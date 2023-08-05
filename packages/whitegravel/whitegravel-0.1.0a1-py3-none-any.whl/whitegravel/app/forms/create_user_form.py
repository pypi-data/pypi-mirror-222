from fastapi import Form

from .base import FormBase


class CreateUserForm(FormBase):
    username: str
    first_name: str
    last_name: str
    email: str

    def __init__(
        self,
        username: str = Form(),
        first_name: str = Form(),
        last_name: str = Form(),
        email: str = Form(),
    ) -> None:
        super().__init__()

        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
