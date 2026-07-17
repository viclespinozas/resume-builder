from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..core.security import get_password_hash, verify_password, create_token_pair, verify_token, create_access_token, get_current_user
from ..core.auth import get_current_active_user
from ..core.config import settings
from ..schemas.auth import LoginRequest, Token, RefreshRequest, UserRegister
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

@router.post("/register", response_model=Token)
async def register(request: UserRegister, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(User).filter(
        (User.username == request.username) | 
        (User.email == request.email)
    ).first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already registered"
        )
    
    # Validate password confirmation
    if request.password != request.confirm_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Passwords do not match"
        )
    
    # Hash the password
    hashed_password = get_password_hash(request.password)
    
    # Create new user
    db_user = User(
        username=request.username,
        email=request.email,
        hashed_password=hashed_password
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # Create token pair for the new user
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    token_pair = create_token_pair(
        data={"sub": db_user.email}, expires_delta=access_token_expires
    )
    
    return token_pair

@router.get("/me")
async def get_current_user_info(current_user: User = Depends(get_current_active_user)):
    # Return current user information
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }
