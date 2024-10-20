from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from backend.settings import settings
# from dotenv import load_dotenv
#
# load_dotenv(dotenv_path='../infra_learn_fastapi/.env')

# SQLALCHEMY_DATABASE_URL = URL.create(
#     drivername='postgresql+psycopg',
#     username=getenv('POSTGRES_USER'),
#     password=getenv('POSTGRES_PASSWORD'),
#     host=getenv('POSTGRES_HOST') or 'localhost',
#     port=int(getenv('POSTGRES_PORT') or 54322),
#     database=getenv('POSTGRES_DB')
# )

SQLALCHEMY_DATABASE_URL = URL.create(
    drivername='postgresql+psycopg',
    username=settings.postgres_user,
    password=settings.postgres_password,
    host=settings.postgres_host,
    port=settings.postgres_port,
    database=settings.postgres_db
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass
