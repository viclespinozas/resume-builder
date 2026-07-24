from pydantic_settings import SettingsConfigDict
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

class Settings(BaseSettings):
    # Database settings
    database_url: str = DATABASE_URL
    
    # JWT settings
    secret_key: str = "your-secret-key-here"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7
    
    # AI settings
    ollama_base_url: str = "http://localhost:11434"
    
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

settings = Settings()