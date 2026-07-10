from fastapi import FastAPI
from .database.session import engine, Base
from .core.config import settings
from .api.v1.api_v1 import api_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Resume Builder API",
    description="AI-powered Resume Builder API for creating and managing professional resumes",
    version="1.0.0"
)

# Include the API routes
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to the Resume Builder API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}