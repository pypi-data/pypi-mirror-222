from datetime import datetime

from .base import BaseClass


class UserClass(BaseClass):
    username: str
    first_name: str
    last_name: str
    email: str
    created_by: str
    updated_by: str
    created_at: datetime
    updated_at: datetime
    last_password_set_at: datetime
    enabled: bool
    comment: str
