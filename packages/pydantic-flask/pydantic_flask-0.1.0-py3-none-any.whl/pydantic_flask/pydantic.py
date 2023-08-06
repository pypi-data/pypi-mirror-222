from __future__ import annotations

import functools
import json
import typing as t

from flask import current_app
from flask import request
from pydantic import BaseModel
from pydantic import validate_call
from pydantic import ValidationError
from werkzeug.datastructures import FileStorage


class Header(str):
    pass


class Cookie(str):
    pass


class JsonModel(BaseModel):
    pass


class FormModel(BaseModel):
    pass


class RequestParser:
    request_field: str | None = None
    converse_type: t.Literal["normal", "dict"] | None = None

    def __init__(self, hints: t.Dict):
        self.hints = hints

    @classmethod
    def condition(cls, var_type: t.Any) -> bool:
        raise NotImplementedError

    @classmethod
    def converse_params(
        cls,
        hints: t.Dict,
        data: t.Dict,
        converse_type: t.Literal["normal", "dict"] | None = None,
    ) -> t.Dict:
        result = {}
        for var, var_type in hints.items():
            value: str | dict | None = data.get(var)
            if value is None:
                continue

            if converse_type == "normal":
                result[var] = var_type(value)
            elif converse_type == "dict":
                result[var] = var_type(**value)
            else:
                result[var] = value
        return result

    @functools.cached_property
    def parsed_hints(self) -> t.Dict:
        return {var: var_type for var, var_type in self.hints.items() if self.condition(var_type)}

    @functools.cached_property
    def data(self) -> t.Dict:
        return getattr(request, self.request_field)

    def parse(self) -> t.Dict:
        return self.converse_params(self.parsed_hints, self.data, self.converse_type) if self.parsed_hints else {}


class QueryParser(RequestParser):
    request_field = "args"

    @classmethod
    def condition(cls, var_type: t.Any) -> bool:
        return not issubclass(var_type, (JsonModel, FormModel, Header, FileStorage))


class JsonParser(RequestParser):
    converse_type = "dict"

    @classmethod
    def condition(cls, var_type: t.Any) -> bool:
        return issubclass(var_type, JsonModel)

    @functools.cached_property
    def data(self) -> t.Dict:
        json_body = request.json if request.is_json else {}
        json_body = {list(self.parsed_hints.keys())[0]: json_body} if len(self.parsed_hints) == 1 else json_body
        return json_body


class HeaderParser(RequestParser):
    request_field = "headers"
    converse_type = "normal"

    @classmethod
    def condition(cls, var_type: t.Any) -> bool:
        return issubclass(var_type, Header)


class CookieParser(RequestParser):
    request_field = "cookies"
    converse_type = "normal"

    @classmethod
    def condition(cls, var_type: t.Any) -> bool:
        return issubclass(var_type, Cookie)


class FileParser(RequestParser):
    request_field = "files"

    @classmethod
    def condition(cls, var_type: t.Any) -> bool:
        return issubclass(var_type, FileStorage)


class FormParser(RequestParser):
    converse_type = "dict"

    @classmethod
    def condition(cls, var_type: t.Any) -> bool:
        return issubclass(var_type, FormModel)

    @functools.cached_property
    def data(self) -> t.Dict:
        return {list(self.parsed_hints)[0]: request.form} if len(self.parsed_hints) == 1 else request.form


def parse_request(hints: t.Dict) -> t.Dict:
    result = {}
    for parser in (
        QueryParser,
        JsonParser,
        HeaderParser,
        CookieParser,
        FileParser,
        FormParser,
    ):
        result.update(**parser(hints).parse())
    return result


def validate(func: t.Callable) -> t.Callable:
    @functools.wraps(func)
    def wrapper(**kwargs):
        try:
            params = parse_request(t.get_type_hints(func))
        except ValidationError as e:
            return {"error": json.loads(e.json())}, current_app.config.get("PYDANTIC_VALIDATION_ERROR_CODE", 400)

        for key in kwargs.keys():
            params.pop(key, None)

        try:
            return validate_call(config=dict(arbitrary_types_allowed=True))(func)(**kwargs, **params)
        except ValidationError as e:
            return {"error": json.loads(e.json())}, current_app.config.get("PYDANTIC_VALIDATION_ERROR_CODE", 400)

    return wrapper
