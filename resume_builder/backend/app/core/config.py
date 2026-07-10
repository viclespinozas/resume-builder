from pydantic_settings import SettingsConfigDict
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Database settings
    database_url: str = "postgresql://user:password@localhost/resume_builder"
    
    # JWT settings
    secret_key: str = "your-secret-key-here"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # AI settings
    ollama_base_url: str = "http://localhost:11434"
    
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

settings = Settings()