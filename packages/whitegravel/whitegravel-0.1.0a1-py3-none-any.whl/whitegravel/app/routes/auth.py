from typing import Annotated
from typing import Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query
from fastapi import HTTPException
from fastapi import status
from fastapi import Request
from fastapi.responses import RedirectResponse

from ..forms.mfa_login_form import MFALoginRequestForm
from ..controllers.user import UserController
from ..classes.base import BasicResponse
from ..classes.user import UserClass
from ..classes.token import TokenClass
from ..classes.token import ActiveTokenDetailList
from ..controllers.token import TokenController
from ..security.auth import AuthorizationBearer

from ..exceptions.base import AuthenticationError
from ..exceptions.controllers import MfaDisabled

from ...constants.app import TOKEN_TYPE_API
from ...constants.app import MAX_VALUE_PAGE

authenticated = AuthorizationBearer()
auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/login", response_model=TokenClass)
async def login_for_access_token(
    request: Request, form_data: Annotated[MFALoginRequestForm, Depends()]
):
    with UserController() as usr_ctrl:
        try:
            usr_ctrl.authenticate_full(
                username=form_data.username,
                password=form_data.password.get_secret_value(),
                mfa_code=form_data.mfa_code,
            )

        except MfaDisabled:
            if form_data.mfa_configuration_redirect_url:
                return RedirectResponse(
                    form_data.mfa_configuration_redirect_url,
                    status_code=status.HTTP_303_SEE_OTHER,
                )

        except AuthenticationError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

    with TokenController() as tkn_ctrl:
        token = tkn_ctrl.create(
            username=form_data.username,
            ipaddress=request.client.host,
            user_agent=request.headers.get("User-Agent"),
        )

        return token


@auth_router.post("/logout", response_model=BasicResponse)
async def close_active_session(
    request: Request,
    current_user: Annotated[UserClass, Depends(authenticated)],
    redirect_url: Annotated[Optional[str], Query()] = None,
    id: Annotated[Optional[str], Query()] = None,
    close_all_sessions: Annotated[Optional[bool], Query()] = False,
):
    authorization_header = request.headers.get("Authorization")

    with TokenController() as tkn_ctrl:
        if close_all_sessions:
            tkn_ctrl.revoke_all(username=current_user.username)
        if id:
            tkn_ctrl.revoke(username=current_user.username, token_id=id)
        else:
            tkn_ctrl.logout(authorization_header=authorization_header)

    if redirect_url:
        return RedirectResponse(url=redirect_url, status_code=status.HTTP_303_SEE_OTHER)

    return BasicResponse(detail="Logged out")


@auth_router.get("/active", response_model=ActiveTokenDetailList)
async def get_active_session(
    request: Request,
    current_user: Annotated[UserClass, Depends(authenticated)],
    page: Annotated[int, Query(ge=1, le=MAX_VALUE_PAGE)] = 1,
    page_size: Annotated[int, Query(ge=25, le=5000)] = 25,
):
    authorization_header = request.headers.get("Authorization")

    with TokenController() as tkn_ctrl:
        current_token = tkn_ctrl.get_current(authorization_header=authorization_header)

        if current_token.type == TOKEN_TYPE_API:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="API Clients cannot query active sessions.",
            )

        total, token_list = tkn_ctrl.list_user_tokens(
            username=current_user.username, page=page, page_size=page_size
        )

        pages = (total // page_size) + 1

        if page > pages:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Page not found"
            )

        return ActiveTokenDetailList(
            total=total, pages=pages, current=current_token, entries=token_list
        )
