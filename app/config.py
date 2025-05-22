from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://postgres:root@localhost:5432/postgres"
    class Config:
        env_file = ".env"

# settings = Settings()

def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()

# setting_var = get_settings()
# print(setting_var.DATABASE_URL)