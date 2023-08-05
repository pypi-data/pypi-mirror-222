from uuid import uuid1
from datetime import datetime, timedelta
from secrets import token_hex

from jose import JWTError
from jose import jwt

from sqlalchemy import desc

from ... import config
from ...constants.app import TOKEN_TYPE_API
from ...constants.app import TOKEN_TYPE_USER
from ...constants.app import ZERO_DATETIME

from ...db.app.tables import UserTable
from ...db.app.tables import TokenTable
from ...db.app.functions import create_engine
from ...db.app.functions import Session

from ..exceptions.base import AuthenticationError
from ..exceptions.base import NotFound
from ..exceptions.base import InvalidOperation

from ..classes.token import TokenClass
from ..classes.token import TokenFullDetailClass

from .base import BaseController
from .user import UserController


class TokenController(BaseController):
    def __init__(self) -> None:
        super().__init__()

    def __enter__(self):
        return super().__enter__()

    def __exit__(self, *exc):
        return super().__exit__(*exc)

    def get_token_detail(self, token: TokenTable):
        return TokenFullDetailClass(
            id=token.id,
            created_at=token.created_at,
            last_ipaddress=token.last_ipaddress,
            last_user_agent=token.last_user_agent,
            last_timestamp=token.last_timestamp,
            type=token.type,
        )

    def verify(self, jwt_token: str, ipaddress: str, user_agent: str):
        SECRET_KEY: str = config.settings.app.JWT_SECRET
        ALGORITHM: str = config.settings.app.JWT_ALGORITHM

        try:
            payload = jwt.decode(jwt_token, SECRET_KEY, algorithms=[ALGORITHM])
            token_id = payload["id"]

        except (JWTError, KeyError):
            raise AuthenticationError("JWT Token Malformed")

        token = (
            self.session.query(TokenTable)
            .filter(
                TokenTable.id == token_id, TokenTable.revoked == False  #! IMPORTANT
            )
            .first()
        )

        if not token:
            raise AuthenticationError("Token not found")

        if token.expiration < datetime.now() and token.type == TOKEN_TYPE_USER:
            raise AuthenticationError("Expired Token")

        if not (token.user.enabled and token.user.mfa_enabled):
            raise AuthenticationError("Invalid user account status")

        token.last_timestamp = datetime.now()
        token.last_ipaddress = ipaddress
        token.last_user_agent = user_agent

        self.session.bulk_save_objects([token])
        self.session.commit()

        try:
            with UserController() as usr_ctrl:
                return usr_ctrl.get(token.username)

        except NotFound:
            raise AuthenticationError("User not found")

    def create(
        self,
        username: str,
        ipaddress: str,
        user_agent: str,
        type: str = TOKEN_TYPE_USER,
    ):
        EXPIRATION: str = config.settings.app.JWT_EXPIRATION
        SECRET_KEY: str = config.settings.app.JWT_SECRET
        ALGORITHM: str = config.settings.app.JWT_ALGORITHM

        with UserController() as user_ctrl:
            user = user_ctrl.get(username)

        id = uuid1().hex
        expiration = datetime.now() + timedelta(minutes=EXPIRATION)

        if type == TOKEN_TYPE_API:
            expiration = ZERO_DATETIME

        payload = {"id": id, "salt": token_hex(32)}

        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        now = datetime.now()

        token_entry = TokenTable(
            id=id,
            username=user.username,
            type=type,
            created_at=now,
            last_ipaddress=ipaddress,
            last_user_agent=user_agent,
            last_timestamp=now,
            expiration=expiration,
        )

        self.session.add(token_entry)
        self.session.commit()

        return TokenClass(access_token=token, token_type="Bearer")

    def revoke(self, username: str, token_id: str):
        token = (
            self.session.query(TokenTable)
            .filter(
                TokenTable.id == token_id,
                TokenTable.username == username,
                TokenTable.revoked == False,  #! IMPORTANT
            )
            .first()
        )

        if token:
            token.revoked = True
            self.session.bulk_save_objects([token])
            self.commit()

    def revoke_all(self, username: str):
        tokens = (
            self.session.query(TokenTable)
            .filter(
                TokenTable.type == TOKEN_TYPE_USER,
                TokenTable.username == username,
                TokenTable.revoked == False,  #! IMPORTANT
            )
            .all()
        )

        for token in tokens:
            token.revoked = True

        self.session.bulk_save_objects(tokens)
        self.session.commit()

    def logout(self, authorization_header: str = None, jwt_token: str = None):
        if not authorization_header and not jwt_token:
            raise InvalidOperation(
                "Some identifier should be provided: authorization_header or jwt_token"
            )

        SECRET_KEY: str = config.settings.app.JWT_SECRET
        ALGORITHM: str = config.settings.app.JWT_ALGORITHM

        if authorization_header:
            splitted_header = authorization_header.split(" ")
            if len(splitted_header) != 2:
                raise InvalidOperation("Authorization header malformed")

            jwt_token = splitted_header[1]

        try:
            payload = jwt.decode(jwt_token, SECRET_KEY, algorithms=[ALGORITHM])
            token_id = payload["id"]
        except (JWTError, KeyError):
            raise InvalidOperation("Authorization token malformed")

        token = (
            self.session.query(TokenTable)
            .filter(
                TokenTable.id == token_id, TokenTable.revoked == False  #! IMPORTANT
            )
            .first()
        )

        if not token:
            return

        if token.type == TOKEN_TYPE_API:
            raise InvalidOperation("API tokens cannot logout.")

        token.revoked = True
        self.session.bulk_save_objects([token])
        self.session.commit()

    def get_current(self, authorization_header: str = None, jwt_token: str = None):
        if not authorization_header and not jwt_token:
            raise InvalidOperation(
                "Some identifier should be provided: authorization_header or jwt_token"
            )

        SECRET_KEY: str = config.settings.app.JWT_SECRET
        ALGORITHM: str = config.settings.app.JWT_ALGORITHM

        if authorization_header:
            splitted_header = authorization_header.split(" ")
            if len(splitted_header) != 2:
                raise InvalidOperation("Authorization header malformed")

            jwt_token = splitted_header[1]

        try:
            payload = jwt.decode(jwt_token, SECRET_KEY, algorithms=[ALGORITHM])
            token_id = payload["id"]
        except (JWTError, KeyError):
            raise InvalidOperation("Authorization token malformed")

        token = self.session.query(TokenTable).filter(TokenTable.id == token_id).one()

        return self.get_token_detail(token)

    def list(self, username: str, page_size: int, page: int, type: str):
        query = (
            self.session.query(TokenTable)
            .filter(
                TokenTable.username == username,
                TokenTable.revoked == False,
                TokenTable.type == type,
            )
            .order_by(desc(TokenTable.last_timestamp))
        )

        entries = query.offset(offset=(page - 1) * page_size).limit(page_size).all()
        total = query.count()

        return total, [self.get_token_detail(entry) for entry in entries]

    def list_user_tokens(self, username: str, page_size: int, page: int):
        return self.list(
            username=username, page_size=page_size, page=page, type=TOKEN_TYPE_USER
        )

    def list_api_tokens(self, username: str, page_size: int, page: int):
        return self.list(
            username=username, page_size=page_size, page=page, type=TOKEN_TYPE_API
        )
