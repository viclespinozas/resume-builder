from fastapi import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

class DatabaseError(Exception):
    """Custom exception for database-related errors"""
    pass

class AuthenticationError(HTTPException):
    """Custom exception for authentication errors"""
    def __init__(self, detail: str = "Authentication failed"):
        super().__init__(status_code=401, detail=detail)

class AuthorizationError(HTTPException):
    """Custom exception for authorization errors"""
    def __init__(self, detail: str = "Authorization failed"):
        super().__init__(status_code=403, detail=detail)

class ValidationError(HTTPException):
    """Custom exception for validation errors"""
    def __init__(self, detail: str = "Validation error"):
        super().__init__(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)