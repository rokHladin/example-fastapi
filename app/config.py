"""
This module contains the configuration settings for the application, 
including database connection details and JWT settings.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict

DB_USER = 'postgres'
DB_PASSWORD = 'postgresapicourse'



class Settings(BaseSettings):
    """
    Configuration settings for the application.
    """

    # It is case insensitive and it does type casting
    # If there is no default value it will look into the environment variables
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str  # It is used to sign the JWT token
    algorithm: str
    access_token_expire_minutes: int

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings() # type: ignore

print(settings.database_username)
