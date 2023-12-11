from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'QRKot - благотворительный фонд.'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET_KEY'

    class Config:
        env_file = '.env'


settings = Settings()