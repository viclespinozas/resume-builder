from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..core.security import get_current_user
from ..models.user import User
from ..database.session import get_db

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
