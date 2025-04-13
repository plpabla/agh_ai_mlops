from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    FASTAPI_SECRET: str

    @field_validator("ENVIRONMENT")
    def validate_environment(cls, value):
        if value not in ["dev", "test", "prod"]:
            raise ValueError("ENVIRONMENT must be one of 'dev', 'test', or 'prod'")
        return value

    @field_validator("FASTAPI_SECRET")
    def validate_fastapi_secret(cls, value):
        if len(value) < 32:
            raise ValueError("FASTAPI_SECRET must be at least 32 characters long")
        return value
