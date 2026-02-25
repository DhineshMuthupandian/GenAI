from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Modular App"
    DATABASE_URL: str = "sqlite:///./test.db"
    SECRET_KEY: str = "supersecret"

    class Config:
        env_file = ".env"

settings = Settings()