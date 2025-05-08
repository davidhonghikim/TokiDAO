import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from typing import Optional

# Load .env file variables
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "TokiDAO API"
    API_V1_STR: str = "/api/v1"
    
    MONGODB_URI: Optional[str] = os.getenv("MONGODB_URI")
    
    # Security settings for JWT
    SECRET_KEY: Optional[str] = os.getenv("SECRET_KEY") # Needed for JWT, generate with: openssl rand -hex 32
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    class Config:
        case_sensitive = True
        # env_file = ".env" # Not needed if load_dotenv() is called directly

settings = Settings()

# Example of how to access settings:
# from app.core.config import settings
# print(settings.MONGODB_URI)
