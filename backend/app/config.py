from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Backend"
    API_V1_STR: str = "/api/v1"

    def get_database_url(self) -> str:
        """
        Get the database URL from environment variables.

        Returns:
            str: The database URL.

        Raises:
            ValueError: If the DATABASE_URL environment variable is not set.
        """
        database_url = os.getenv("DATABASE_URL")

        if database_url is None:
            raise ValueError("DATABASE_URL environment variable not set")

        return database_url
    

settings = Settings()