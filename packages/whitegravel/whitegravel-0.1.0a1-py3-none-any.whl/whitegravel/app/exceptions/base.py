from whitegravel.exceptions.base import whitegravelError


class AppError(whitegravelError):
    pass


class NotFound(AppError):
    pass


class ForbiddenOperation(AppError):
    pass


class AuthenticationError(AppError):
    pass


class InvalidOperation(AppError):
    pass
