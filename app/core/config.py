"""Configuration settings for the application."""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_KEY_NAME: str = ""
    AZURE_STORAGE_CONNECTION_STRING: str = "DefaultAzureConnectionString"
    AZURE_CONTAINER_NAME: str = "your-default-container-name"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()



