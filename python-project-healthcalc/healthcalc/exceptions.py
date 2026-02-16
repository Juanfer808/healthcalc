class InvalidHealthDataException(Exception):
    """Exception raised when health data is not valid."""
    def __init__(self, message):
        super().__init__(message)