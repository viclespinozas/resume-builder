import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.core.security import verify_password, get_password_hash
from app.models.user import User
from app.database.session import get_db

client = TestClient(app)

# Test user data
TEST_USER_DATA = {
    "username": "testuser",
    "email": "test@example.com",
    "password": "TestPass123",
    "confirm_password": "TestPass123"
}

@pytest.fixture(scope="module")
def test_user(db_session: Session):
    """Create a test user for testing authentication"""
    # Check if user exists
    existing_user = db_session.query(User).filter(
        (User.username == TEST_USER_DATA["username"]) | 
        (User.email == TEST_USER_DATA["email"])
    ).first()
    
    if not existing_user:
        # Create new user
        hashed_password = get_password_hash(TEST_USER_DATA["password"])
        user = User(
            username=TEST_USER_DATA["username"],
            email=TEST_USER_DATA["email"],
            hashed_password=hashed_password
        )
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)
        return user
    else:
        return existing_user

def test_register_user():
    """Test user registration"""
    response = client.post("/auth/register", json=TEST_USER_DATA)
    
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"

def test_login_user():
    """Test user login"""
    login_data = {
        "username": TEST_USER_DATA["username"],
        "password": TEST_USER_DATA["password"]
    }
    
    response = client.post("/auth/login", data=login_data)
    
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_credentials():
    """Test login with invalid credentials"""
    login_data = {
        "username": "invaliduser",
        "password": "wrongpassword"
    }
    
    response = client.post("/auth/login", data=login_data)
    
    assert response.status_code == 401

def test_refresh_token():
    """Test token refresh functionality"""
    # First login to get tokens
    login_data = {
        "username": TEST_USER_DATA["username"],
        "password": TEST_USER_DATA["password"]
    }
    
    login_response = client.post("/auth/login", data=login_data)
    assert login_response.status_code == 200
    
    refresh_token = login_response.json()["refresh_token"]
    
    # Now try to refresh
    refresh_response = client.post("/auth/refresh", json={"refresh_token": refresh_token})
    
    assert refresh_response.status_code == 200
    data = refresh_response.json()
    assert "access_token" in data
    assert "refresh_token" in data

def test_get_current_user():
    """Test getting current user info"""
    # First login to get tokens
    login_data = {
        "username": TEST_USER_DATA["username"],
        "password": TEST_USER_DATA["password"]
    }
    
    login_response = client.post("/auth/login", data=login_data)
    assert login_response.status_code == 200
    
    access_token = login_response.json()["access_token"]
    
    # Now try to get current user info
    response = client.get("/auth/me", headers={"Authorization": f"Bearer {access_token}"})
    
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "username" in data
    assert "email" in data

def test_register_duplicate_user():
    """Test registering with duplicate username/email"""
    # Try to register same user again
    response = client.post("/auth/register", json=TEST_USER_DATA)
    
    assert response.status_code == 400