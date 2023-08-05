#
#
# voice-skill-sdk
#
# (C) 2021, Deutsche Telekom AG
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#

"""Utility functions"""

import re
import sys
import time
import asyncio
import inspect
import datetime
import threading
import contextlib
import unittest.mock
import importlib.util
from functools import partial
from contextvars import copy_context
from concurrent.futures import ThreadPoolExecutor
from types import ModuleType
from typing import (
    Any,
    Awaitable,
    Callable,
    Dict,
    List,
    Text,
    TypeVar,
    Union,
)

import orjson
import pydantic
import nest_asyncio
from pydantic import root_validator, validator, ValidationError  # noqa
from pydantic.utils import lenient_issubclass
import uvicorn


T = TypeVar("T")
DEFAULT_LOCALE = "de"


def camel_to_snake(name):
    """
    Convert CamelCase to snake_case

    :param name:
    :return:
    """
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def snake_to_camel(name):
    """
    Convert snake_case to CamelCase

    :param name:
    :return:
    """
    reg_ex = re.compile(r"_+[a-z0-9]")
    return reg_ex.sub(lambda x: x.group(0)[1].upper(), name)


def orjson_dumps(v, *, default):
    """
    orjson.dumps returns bytes, to match standard json.dumps we need to decode

    :param v:
    :param default:
    :return:
    """
    return orjson.dumps(v, default=default).decode()


class Server(uvicorn.Server):
    """Uvicorn server implementing "run_in_thread" context manager:

    >>> server = Server("app:app", port=4242)
    >>> with server.run_in_thread():
    >>>     # Server started.
    >>>     ...
    >>> # Server stopped

    """

    WAIT_TIME = 1e-3

    def __init__(self, *args, **kwargs):
        if "loop" not in kwargs:
            kwargs.update(dict(loop="asyncio"))
        config = uvicorn.Config(*args, **kwargs)
        super().__init__(config)

    @contextlib.contextmanager
    def run_in_thread(self):
        thread = threading.Thread(target=self.run)
        thread.start()
        try:
            while not self.started:
                time.sleep(Server.WAIT_TIME)
            yield
        finally:
            self.should_exit = True
            thread.join()


def reload_recursive(module: ModuleType) -> ModuleType:
    """
    Recursively reload a runner module (app.py) with submodules

    :param module:
    :return:
    """
    reloaded = set()

    def reload_parent(module_name):
        parent = sys.modules[module_name]
        if parent not in reloaded:
            reloaded.add(parent)
            importlib.reload(parent)

    def visit(m):
        reloaded.add(m)
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if isinstance(attr, Callable):
                reload_parent(attr.__module__)
            if isinstance(attr, ModuleType):
                name = attr.__name__
                dot = name.rfind(".")
                if dot > 0:
                    reload_parent(name[:dot])
                elif attr not in reloaded:
                    visit(attr)
        importlib.reload(m)
        return m

    return visit(module)


class ContextVarExecutor(ThreadPoolExecutor):
    """Copy existing contextVars before executing"""

    def submit(self, *args, **kwargs):
        ctx = copy_context()

        return super().submit(ctx.run, *args, **kwargs)


async def run_in_executor(func: Callable[..., T], *args: Any, **kwargs: Any) -> T:
    """
    Run a synchronous function in a thread pool to prevent blocking

    :param func:
    :param args:
    :param kwargs:
    :return:
    """
    loop = asyncio.get_running_loop()

    return await loop.run_in_executor(
        ContextVarExecutor(), partial(func, *args, **kwargs)
    )


def run_until_complete(func: Awaitable[T]) -> T:
    """
    Run an asynchronous function in synchronous context

    :param func:
    :return:
    """
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    if loop.is_running():
        nest_asyncio.apply(loop)

    return loop.run_until_complete(func)


class BaseModel(pydantic.BaseModel):
    """
    Override Pydantic's BaseModel defaults:

        - use faster orjson for objects serialization

        - make all instances immutable
            (with an exception of `responses.Result` - that is mutable for backward compatibility)

        - allow objects population by the model attribute

        - use enum value instead of raw enums when populating properties

    """

    class Config:
        """Alter default config for base models"""

        # Use orjson to serialize
        json_dumps = orjson_dumps

        # Make all model instances "faux-immutable" by default
        allow_mutation = False

        # Allow objects population by the model attribute, as well as the alias
        allow_population_by_field_name = True

        # Populate models with the value property of enums, rather than the raw enum
        use_enum_values = True

    def dict(self, *args, **kwargs) -> Dict[Text, Any]:
        """
        Alter parent defaults when exporting:

            - exclude "None" values
            - export fields by alias

        """
        params = {
            "exclude_none": kwargs["exclude_none"]
            if "exclude_none" in kwargs
            else True,
            "by_alias": kwargs["by_alias"] if "by_alias" in kwargs else True,
        }

        return super().dict(*args, **{**kwargs, **params})


class CamelModel(BaseModel):
    """CamelModel will use camelCase aliases for snake_case fields"""

    class Config:
        """Set `snake_to_camel` as alias generator function"""

        alias_generator = snake_to_camel


def attrs_examples(intent: Callable) -> Dict[str, List]:
    """
    Create attribute samples for intent

    :param intent:
    :return:
    """

    from skill_sdk.intents import AttributeV2, Request

    # Extract parameter arguments from intent implementation
    parameters = {
        name: param
        for name, param in inspect.signature(intent).parameters.items()
        if not lenient_issubclass(param.annotation, Request)
    }

    # 'timezone' is always present
    if "timezone" not in parameters:
        parameters["timezone"] = inspect.Parameter(
            "timezone", inspect.Parameter.KEYWORD_ONLY, default="UTC"
        )

    def value(param):
        """Try to set value to an attribute"""
        return (
            param.default
            if param.default and param.default != inspect.Parameter.empty
            else "value"
        )

    attrs_v2 = {
        name: [AttributeV2(value=value(param), id=0).dict()]
        for name, param in parameters.items()
    }

    return attrs_v2


#
#   Unit test helpers:
#

datetime_class = datetime.datetime


def mock_datetime_now(target, dt):
    """
    Patch datetime.datetime.now with __instancecheck__
    """

    class DatetimeSubclassMeta(type):
        """Metaclass to mock __instancecheck__"""

        @classmethod
        def __instancecheck__(mcs, obj):  # NOSONAR
            return isinstance(obj, datetime_class)

    class BaseMockedDatetime(datetime_class):
        """Patch the original datetime.datetime.now"""

        @classmethod
        def now(cls, tz=None):
            return target.replace(tzinfo=tz)

        @classmethod
        def utcnow(cls):
            return target

    dt_mock = DatetimeSubclassMeta("datetime", (BaseMockedDatetime,), {})
    return unittest.mock.patch.object(dt, "datetime", dt_mock)


def mock_date_today(now):
    """
    Patch datetime.date.today
    """

    class MockedDate(datetime.date):
        @classmethod
        def today(cls):
            return now

    return unittest.mock.patch.object(datetime, "date", MockedDate)


def create_request(
    intent: Text, session: Union[CamelModel, Dict[Text, Text]] = None, **kwargs
):
    """
    Skill invoke request factory: used in unit tests to mock a skill invoke request

    :param intent:      Intent name
    :param session:     Session (or session attributes)
    :param kwargs:      Keyword arguments are forwarded to create_context factory
    :return:
    """

    from skill_sdk.__version__ import __spi_version__
    from skill_sdk.intents import Request, Session
    from skill_sdk.responses import SessionResponse

    example: Dict = Session.Config.schema_extra["example"]
    if isinstance(session, Session):
        _session = session.copy()
    elif isinstance(session, SessionResponse):
        _session = Session(
            **{
                **dict(id=example["id"], new=False),
                **dict(attributes=session.attributes),
            }
        )
    elif isinstance(session, Dict):
        _session = Session(
            **{**dict(id=example["id"], new=example["new"]), **dict(attributes=session)}
        )
    else:
        _session = Session(**example)

    return Request(
        intent=intent,
        session=_session,
        spi_version=__spi_version__,
        **map_attributes(**kwargs),
    )


def test_request(
    intent: Text,
    session: Union[CamelModel, Dict[Text, Text]] = None,
    translation=None,  # noqa: don't want to import i18n for type hinting `Translations`
    **kwargs,
):
    """
    Context manager to setup global request object for unit tests

    :param intent:      Intent name for the test request
    :param session:     Session attributes
    :param translation: Optional translations
    :param kwargs:      The rest of kwargs goes to `create_context`

    :return:
    """
    from skill_sdk.i18n import Translations
    from skill_sdk.intents.request import RequestContextVar

    translations = kwargs.pop("translation", Translations())

    request = create_request(intent, session=session, **kwargs).with_translation(
        translations
    )

    return RequestContextVar(request=request)


def map_attributes(
    *,
    locale: Text = DEFAULT_LOCALE,
    skill_id: Text = None,
    svh_access_token: Text = None,
    client_type_name: Text = None,
    **kwargs,
):
    """
    Extract attributes for the request

    :param locale:      Request locale
    :param skill_id:    Optional skill ID
    :param svh_access_token:      SVH tokens (if requires)
    :param client_type_name:    Client type (mini/premium/etc)
    :param kwargs:      Attributes(V2)
    :return:
    """

    from skill_sdk.intents import AttributeV2

    def parse(_: Any) -> AttributeV2:
        """Try to create AttributeV2 from any string"""

        try:
            attr_v2: AttributeV2 = AttributeV2(_)
        except (AttributeError, TypeError, ValidationError, ValueError):
            attr_v2 = AttributeV2({"id": 0, "value": _})
        return attr_v2

    attributes_v2 = {
        key: [parse(each) for each in value]
        if isinstance(value, (list, tuple))
        else [parse(value)]
        for key, value in kwargs.items()
        if value is not None
    }

    # 'timezone' is always present
    if "timezone" not in attributes_v2:
        attributes_v2["timezone"] = [parse("Europe/Berlin")]

    return {
        "skill_id": skill_id or "",
        "attributes": attributes_v2 or {},
        "svh_access_token": svh_access_token or "",
        "locale": locale,
        "client_type_name": client_type_name,
    }
