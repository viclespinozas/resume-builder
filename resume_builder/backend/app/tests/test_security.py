import pytest
from app.core.security import verify_password, get_password_hash, create_access_token, create_refresh_token, create_token_pair

def test_password_hashing():
    """Test password hashing and verification"""
    password = "TestPass123"
    hashed = get_password_hash(password)
    
    assert verify_password(password, hashed) == True
    assert verify_password("wrongpassword", hashed) == False

def test_create_access_token():
    """Test access token creation"""
    token_data = {"sub": "123", "username": "testuser"}
    token = create_access_token(token_data)
    
    assert token is not None
    assert isinstance(token, str)

def test_create_refresh_token():
    """Test refresh token creation"""
    token_data = {"sub": "123", "username": "testuser"}
    token = create_refresh_token(token_data)
    
    assert token is not None
    assert isinstance(token, str)

def test_create_token_pair():
    """Test creating both access and refresh tokens"""
    token_pair = create_token_pair(123, "testuser")
    
    assert "access_token" in token_pair
    assert "refresh_token" in token_pair
    assert token_pair["token_type"] == "bearer"