from fastapi.security import HTTPBearer
from fastapi.security.utils import get_authorization_scheme_param
from fastapi import Request
from fastapi import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

from ..controllers.token import TokenController
from ..exceptions.base import AuthenticationError


class AuthorizationBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(AuthorizationBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        authorization = request.headers.get("Authorization")
        scheme, credentials = get_authorization_scheme_param(authorization)

        if not (authorization and scheme and credentials):
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Authentication header missing.",
            )

        if scheme.lower() != "bearer":
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication scheme.",
            )

        user = self.verify(credentials, request)
        if not user:
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED, detail="Not authenticated."
            )

        return user

    def verify(self, token: str, request: Request):
        try:
            with TokenController() as tkn_ctrl:
                user = tkn_ctrl.verify(
                    jwt_token=token,
                    ipaddress=request.client.host,
                    user_agent=request.headers.get("User-Agent"),
                )

                return user

        except AuthenticationError:
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
