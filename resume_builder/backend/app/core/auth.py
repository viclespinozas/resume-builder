from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.models.user import User
from app.database.session import get_db

def get_current_active_user(token: str, db: Session = Depends(get_db)) -> User:
    """
    Get current user from token and verify they exist in database.
    This is a dependency that can be used to protect routes.
    """
    payload = get_current_user(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user_id = int(payload.get("sub"))
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user

def get_current_active_user_from_request(request):
    """
    Extract current user from request headers.
    This is used for the /me endpoint to avoid DB dependency.
    """
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization header",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    token = auth_header.split(" ")[1]
    payload = get_current_user(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return payload