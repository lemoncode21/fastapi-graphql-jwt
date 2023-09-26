import typing

from strawberry.permission import BasePermission
from strawberry.types import Info
from Middleware.JWTManager import JWTManager


class IsAuthenticated(BasePermission):
    message = "User is not Authenticated"

    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        request = info.context["request"]
        # Access headers authentication
        authentication = request.headers["authentication"]
        if authentication:
            token = authentication.split("Bearer ")[-1]
            return JWTManager.verify_jwt(token)
        return False
