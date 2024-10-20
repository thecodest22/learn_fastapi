from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    debug: bool
    postgres_host: str = 'localhost'
    postgres_port: int = 54322
    postgres_db: str
    postgres_user: str
    postgres_password: str

    model_config = SettingsConfigDict(
        env_file='../infra_learn_fastapi/.env',
        env_file_encoding='utf-8',
        extra='ignore',
        validate_default=False
    )

settings = Settings()
print(settings)
