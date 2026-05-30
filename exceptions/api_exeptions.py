
class ApiError(Exception):
    pass
class NotFoundError(ApiError):
    pass
class ForbiddenError(ApiError):
    pass
class ValidationError(ApiError):
    pass
