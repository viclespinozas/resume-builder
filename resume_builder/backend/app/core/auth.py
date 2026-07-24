from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..core.security import get_current_user
from ..models.user import User
from ..database.session import get_db
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_active_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db),
    ) -> User:
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
    
    email = payload.get("sub")
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user
