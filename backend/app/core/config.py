"""Application Configuration"""

from pydantic_settings import BaseSettings
from typing import Optional
import os


def ensure_data_directory(path: str) -> None:
    """Ensure data directory exists for database"""
    db_dir = os.path.dirname(path)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)


class Settings(BaseSettings):
    """Application Settings"""
    
    # Application
    APP_NAME: str = "AI Enterprise Operating System"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    # API Settings
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_PREFIX: str = "/api/v1"
    
    # Database - SQLite (Streamlit Cloud compatible)
    DATABASE_PATH: str = "./data/ai_enterprise.db"
    
    # JWT Authentication
    JWT_SECRET_KEY: str = "your-secret-key-change-this-in-production"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # ML Models
    MODEL_STORAGE_PATH: str = "./models"
    MODEL_VERSION: str = "1.0.0"
    
    # Cloud Provider
    CLOUD_PROVIDER: str = "aws"
    AWS_ACCESS_KEY_ID: Optional[str] = None
    AWS_SECRET_ACCESS_KEY: Optional[str] = None
    AWS_REGION: str = "us-east-1"
    
    @property
    def database_url(self) -> str:
        """Get SQLite connection URL"""
        return f"sqlite:///{self.DATABASE_PATH}"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

# Ensure data directory exists at module load time
ensure_data_directory(settings.DATABASE_PATH)
