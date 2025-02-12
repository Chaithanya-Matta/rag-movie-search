from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    OPENAI_API_KEY: os.getenv("OPENAI_API_KEY")
    VECTOR_DB_URL: os.getenv("VECTOR_DB_URL")

    class Config:
        env_file = ".env"

settings = Settings()
