import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "EcoDrop API"
    PROJECT_VERSION: str = "1.0.0"
    
    # Database configuration - defaults to SQLite for local dev
    DB_TYPE: str = os.getenv("DB_TYPE", "sqlite")
    
    if DB_TYPE == "sqlite":
        DATABASE_URL: str = "sqlite:///./ecodrop.db"
    else:
        POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
        POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "password")
        POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
        POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")
        POSTGRES_DB: str = os.getenv("POSTGRES_DB", "ecodrop")
        DATABASE_URL: str = os.getenv(
            "DATABASE_URL", 
            f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
        )

    SECRET_KEY: str = os.getenv("SECRET_KEY", "DEVELOPMENT_SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()
