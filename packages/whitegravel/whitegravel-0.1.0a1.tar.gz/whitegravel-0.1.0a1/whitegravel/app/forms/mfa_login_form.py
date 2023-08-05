from typing import Optional

from fastapi import Form
from pydantic import SecretStr

from .base import FormBase


class MFALoginRequestForm(FormBase):
    username: str
    password: SecretStr
    mfa_code: str
    mfa_configuration_redirect_url: Optional[str]

    def __init__(
        self,
        username: str = Form(),
        password: SecretStr = Form(),
        mfa_code: str = Form(),
        mfa_configuration_redirect_url: Optional[str] = Form(default=None),
    ) -> None:
        super().__init__()

        self.username = username
        self.password = password
        self.mfa_code = mfa_code
        self.mfa_configuration_redirect_url = mfa_configuration_redirect_url
