from datetime import datetime


from ...db.app.tables import UserTable

from ...constants.app import PASSWORD_POLICY
from ...constants.app import ZERO_DATETIME
from ...constants.app import RESERVED_USERNAMES

from ..classes.user import UserClass

from ..security.passwords import verify_password
from ..security.passwords import get_password_hash
from ..security.passwords import is_strong_password
from ..security.passwords import generate_password

from ..security.mfa import verify_mfa
from ..security.mfa import generate_secret


from ..exceptions.base import NotFound
from ..exceptions.base import AuthenticationError
from ..exceptions.base import ForbiddenOperation

from ..exceptions.controllers import WeakPassword
from ..exceptions.controllers import MfaAlreadyEnabled
from ..exceptions.controllers import MfaInvalidCode
from ..exceptions.controllers import MfaDisabled

from .base import BaseController


class UserController(BaseController):
    def __init__(self) -> None:
        super().__init__()

    def __read_entry(self, username: str):
        username = username.lower()

        user = self.session.get(UserTable, username)
        if not user:
            raise NotFound(f"User '{username}' not found.")

        return user

    def __enter__(self):
        return super().__enter__()

    def __exit__(self, *exc):
        return super().__exit__(*exc)

    @staticmethod
    def get_user_class(user: UserTable):
        user_class = UserClass(
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            created_by=user.created_by,
            updated_by=user.updated_by,
            created_at=user.created_at,
            updated_at=user.updated_at,
            enabled=user.enabled,
            comment=user.comment,
            last_password_set_at=user.last_password_set_at,
        )

        return user_class

    def verify_password(self, username: str, password: str):
        if username in RESERVED_USERNAMES:
            raise ForbiddenOperation("Reserved usernames cannot be authenticated")

        user = self.__read_entry(username=username)
        return verify_password(hashed_password=user.password, plain_password=password)

    def verify_mfa(self, username: str, code: str):
        if username in RESERVED_USERNAMES:
            raise ForbiddenOperation("Reserved usernames cannot be authenticated")

        user = self.__read_entry(username=username)
        return verify_mfa(secret=user.mfa, code=code)

    def authenticate_pwd(self, username: str, password: str):
        if username in RESERVED_USERNAMES:
            raise ForbiddenOperation("Reserved usernames cannot be authenticated")

        user_entry = self.__read_entry(username=username)
        user = self.get_user_class(user=user_entry)

        if (
            user.last_password_set_at
            != ZERO_DATETIME  # The user must be set the password
            and self.verify_password(username=username, password=password)
        ):
            return user

        raise AuthenticationError("Unauthorized")

    def authenticate_full(self, username: str, password: str, mfa_code: str):
        if username in RESERVED_USERNAMES:
            raise ForbiddenOperation("Reserved usernames cannot be authenticated")

        user = self.__read_entry(username=username)

        #! IMPORTANT Check if MFA was configured.
        #! ############################################################################
        if not user.mfa_enabled:
            raise MfaDisabled("MFA is disabled. Please configure MFA before continue.")
        #! ----------------------------------------------------------------------------

        ok_password = verify_password(
            hashed_password=user.password, plain_password=password
        )
        ok_mfa = verify_mfa(secret=user.mfa, code=mfa_code)

        if ok_password and ok_mfa:
            return self.get_user_class(user=user)

        raise AuthenticationError("Unauthorized")

    def get_mfa(self, username: str, password: str):
        if username in RESERVED_USERNAMES:
            raise ForbiddenOperation("Reserved usernames cannot be authenticated")

        self.authenticate_pwd(username=username, password=password)

        user_entry = self.__read_entry(username=username)
        if user_entry.mfa_enabled:
            raise MfaAlreadyEnabled(
                "The MFA already enabled. To retrieve a MFA "
                "Secret the MFA should be reseted."
            )

        return user_entry.mfa

    def enable_mfa(self, username: str, password: str, code: str):
        if username in RESERVED_USERNAMES:
            raise ForbiddenOperation("Reserved usernames cannot be authenticated")

        self.authenticate_pwd(username=username, password=password)

        user_entry = self.__read_entry(username=username)
        ok_mfa = verify_mfa(secret=user_entry.mfa, code=code)

        if not ok_mfa:
            raise MfaInvalidCode(
                "The MFA code is invalid. Please try again or reset MFA."
            )

        user_entry.mfa_enabled = True
        self.session.bulk_save_objects([user_entry])
        self.commit()

    def get(self, username: str):
        user = self.__read_entry(username=username)
        return self.get_user_class(user=user)

    def create(
        self,
        current_username: str,
        username: str,
        first_name: str,
        last_name: str,
        email: str,
    ):
        if username in RESERVED_USERNAMES:
            raise ForbiddenOperation("The username is reserved")

        current_user_entry = self.__read_entry(current_username)
        now = datetime.now()

        created_by = current_user_entry.username
        updated_by = current_user_entry.username
        created_at = now
        updated_at = now
        password = generate_password(128)

        #! IMPORTANT: Hash and salt password before save it
        #! ################################################
        password = get_password_hash(password=password)
        #! ------------------------------------------------

        user = UserTable(
            username=username.lower(),
            first_name=first_name,
            last_name=last_name,
            email=email.lower(),
            created_by=created_by,
            updated_by=updated_by,
            created_at=created_at,
            updated_at=updated_at,
            password=password,
            last_password_set_at=ZERO_DATETIME,
            mfa=generate_secret(),
        )

        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

        return self.get_user_class(user=user)

    def update_password(self, username: str, user_mfa_code: str):
        if username in RESERVED_USERNAMES:
            raise ForbiddenOperation("Reserved usernames cannot be authenticated")

        if self.verify_mfa(username=username, code=user_mfa_code):
            raise MfaInvalidCode("The MFA code is invalid.")

        now = datetime.now()

        #! IMPORTANT: Check password policy
        #! ################################################
        if not is_strong_password(password=password, **PASSWORD_POLICY):
            raise WeakPassword(
                "The password is weak. Password policy requires: "
                "lowercase, uppercase, symbols, numbers and minimun "
                "length of 8 chars."
            )
        #! ------------------------------------------------

        #! IMPORTANT: Hash and salt password before save it
        #! ################################################
        password = get_password_hash(password=password)
        #! ------------------------------------------------

        user = self.__read_entry(username=username)

        user.password = password
        user.updated_by = username
        user.updated_at = now
        user.last_password_set_at = now

        self.session.bulk_save_objects([user])
        self.commit()

    def set_mfa(self, username: str, user_mfa_code: str):
        if username in RESERVED_USERNAMES:
            raise ForbiddenOperation("Reserved usernames cannot be authenticated")

        if self.verify_mfa(username=username, code=user_mfa_code):
            raise MfaInvalidCode("The MFA code is invalid.")

        user = self.__read_entry(username=username)

        user.mfa = generate_secret()
        user.mfa_enabled = False

        self.session.bulk_save_objects([user])
        self.commit()

    def update(
        self,
        current_username: str,
        username: str,
        first_name: str = None,
        last_name: str = None,
        email: str = None,
        enabled: bool = None,
    ):
        self.__read_entry(username=username)

        updates = {
            k: v
            for k, v in dict(
                first_name=first_name, last_name=last_name, email=email, enabled=enabled
            ).items()
            if v is not None
        }

        if username in RESERVED_USERNAMES and email:
            updates = dict(
                email=email,
            )

        if not updates:
            return

        updates.update(updated_at=datetime.now(), updated_by=current_username)

        self.session.bulk_update_mappings(UserTable, updates)
        self.commit()
