from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # PostgreSQL Database
    DATABASE_URL: str
    
    # Firebase Configuration (Only for Google Sign-in)
    FIREBASE_PROJECT_ID: str
    FIREBASE_PRIVATE_KEY: str
    FIREBASE_CLIENT_EMAIL: str
    FIREBASE_DATABASE_URL: str

    # JWT Configuration
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # API Configuration
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = "Balance Scale Addition API"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
