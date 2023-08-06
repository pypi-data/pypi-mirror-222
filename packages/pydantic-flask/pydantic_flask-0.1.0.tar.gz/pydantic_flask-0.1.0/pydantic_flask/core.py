import typing as t
from abc import ABC

from flask import Blueprint
from flask import Flask
from flask.scaffold import T_route, Scaffold

from pydantic_flask.pydantic import validate


class PydanticScaffold(Scaffold, ABC):
    def route(self, rule: str, **options: t.Any) -> t.Callable[[T_route], T_route]:
        def decorator(f: T_route) -> T_route:
            endpoint = options.pop("endpoint", None)
            self.add_url_rule(rule, endpoint, validate(f), **options)
            return f

        return decorator


class PydanticFlask(PydanticScaffold, Flask):
    pass


class PydanticBlueprint(PydanticScaffold, Blueprint):
    pass
