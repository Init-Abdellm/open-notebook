class OneticError(Exception):
    """Base exception class for ONETIC errors."""

    pass


class DatabaseOperationError(OneticError):
    """Raised when a database operation fails."""

    pass


class UnsupportedTypeException(OneticError):
    """Raised when an unsupported type is provided."""

    pass


class InvalidInputError(OneticError):
    """Raised when invalid input is provided."""

    pass


class NotFoundError(OneticError):
    """Raised when a requested resource is not found."""

    pass


class AuthenticationError(OneticError):
    """Raised when there's an authentication problem."""

    pass


class ConfigurationError(OneticError):
    """Raised when there's a configuration problem."""

    pass


class ExternalServiceError(OneticError):
    """Raised when an external service (e.g., AI model) fails."""

    pass


class RateLimitError(OneticError):
    """Raised when a rate limit is exceeded."""

    pass


class FileOperationError(OneticError):
    """Raised when a file operation fails."""

    pass


class NetworkError(OneticError):
    """Raised when a network operation fails."""

    pass


class NoTranscriptFound(OneticError):
    """Raised when no transcript is found for a video."""

    pass
