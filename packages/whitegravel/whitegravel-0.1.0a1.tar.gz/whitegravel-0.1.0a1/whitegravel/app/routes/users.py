from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Path
from fastapi import HTTPException
from fastapi import status

from ..security.auth import AuthorizationBearer
from ..controllers.user import UserController
from ..classes.user import UserClass
from ..forms.create_user_form import CreateUserForm

from ..exceptions.base import NotFound

authenticated = AuthorizationBearer()
users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.post("/create", response_model=UserClass)
async def read_users_by_username(
    form_data: Annotated[CreateUserForm, Depends()],
    current_user: Annotated[UserClass, Depends(authenticated)],
):
    with UserController() as usr_ctrl:
        user = usr_ctrl.create(
            current_username=current_user.username, **form_data.dict()
        )

    return user.export()


@users_router.get("/me", response_model=UserClass)
async def read_users_me(current_user: Annotated[UserClass, Depends(authenticated)]):
    return current_user.export()


@users_router.get("/{username}", response_model=UserClass)
async def read_users_by_username(
    username: Annotated[str, Path(title="The username to read")],
    current_user: Annotated[UserClass, Depends(authenticated)],
):
    with UserController() as usr_ctrl:
        try:
            user = usr_ctrl.get(username=username)
        except NotFound:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"The username '{username}' was not found",
            )

    return user.export()
