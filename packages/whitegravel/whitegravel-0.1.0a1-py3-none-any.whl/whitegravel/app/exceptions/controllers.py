from .base import AppError


class UserControllerError(AppError):
    pass


class WeakPassword(UserControllerError):
    pass


class MfaAlreadyEnabled(UserControllerError):
    pass


class MfaInvalidCode(UserControllerError):
    pass


class MfaDisabled(UserControllerError):
    pass
