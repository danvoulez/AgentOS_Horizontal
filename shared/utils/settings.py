
from pydantic import BaseSettings, Field, HttpUrl, validator

class Settings(BaseSettings):
    mongo_uri: str = Field(..., env="MONGO_URI")
    redis_url: str = Field(..., env="REDIS_URL")
    llm_api_key: str = Field(..., env="LLM_API_KEY")
    env: str = Field("dev", env="ENV")

settings = Settings()
