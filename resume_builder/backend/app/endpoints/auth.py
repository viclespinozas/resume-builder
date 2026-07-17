from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..core.security import get_password_hash, verify_password, create_token_pair, verify_token, create_access_token
from ..core.config import settings
from ..schemas.auth import LoginRequest, Token, RefreshRequest
from ..models.user import User
from ..database.session import get_db
from datetime import timedelta

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    # Find user by email
    db_user = db.query(User).filter(User.email == request.email).first()
    
    if not db_user or not verify_password(request.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_token_pair(
        data={"sub": db_user.email}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/refresh")
async def refresh(request: RefreshRequest):
    payload = verify_token(request.refresh_token)
    if payload.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Invalid token type")
    new_access_token = create_access_token(data={"sub": payload["sub"]})
    return {"access_token": new_access_token, "token_type": "bearer"}