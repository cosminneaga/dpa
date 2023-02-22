class Error(Exception):
    pass


class UserExists(Error):
    pass


class UserNotFound(Error):
    pass


class ApiKeyError(Error):
    pass


class NotFound(Error):
    pass
