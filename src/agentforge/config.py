from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mode: Literal["deterministic", "langchain"] = "deterministic"
    model: str = "openai:gpt-5.5"
    max_tool_calls: int = 6
    require_approval_for_writes: bool = True

    model_config = SettingsConfigDict(env_prefix="AGENTFORGE_", env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
