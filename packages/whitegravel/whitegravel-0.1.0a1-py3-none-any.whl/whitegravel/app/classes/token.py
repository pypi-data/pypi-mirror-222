from datetime import datetime

from .base import BaseClass


class TokenClass(BaseClass):
    access_token: str
    token_type: str


class TokenDetailClass(BaseClass):
    id: str
    created_at: datetime
    last_ipaddress: str
    last_user_agent: str
    last_timestamp: datetime
    type: str


class TokenFullDetailClass(TokenDetailClass):
    type: str


class ActiveTokenDetailList(BaseClass):
    total: int
    pages: int
    current: TokenDetailClass
    entries: list[TokenDetailClass]
