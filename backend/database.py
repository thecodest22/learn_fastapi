from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String, create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import (DeclarativeBase, Mapped, mapped_column,
                            relationship, sessionmaker)

from dotenv import dotenv_values

env = dotenv_values(dotenv_path='../infra_learn_fastapi/.env')

SQLALCHEMY_DATABASE_URL = URL.create(
    drivername='postgresql+psycopg',
    username=env['POSTGRES_USER'],
    password=env['POSTGRES_PASSWORD'],
    host=env.get('POSTGRES_HOST') or 'localhost',
    port=env.get('POSTGRES_PORT') or '54322',
    database=env['POSTGRES_DB']
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'my_app.user'

    pk: Mapped[int] = mapped_column(
        primary_key=True
    )
    first_name: Mapped[str] = mapped_column(
        String(30)
    )
    last_name: Mapped[str | None]

    # orders: Mapped[list['Order']] = relationship(
    #     back_populates='user',
    #     cascade='all, delete-orphan'
    # )

    def __repr__(self) -> str:
        return (f'User(pk={self.pk!r}, first_name={self.first_name!r},'
                f' last_name={self.last_name!r})')


# class Order(Base):
#     __tablename__ = 'my_app.orders'
#
#     pk: Mapped[int] = mapped_column(
#         primary_key=True
#     )
#     number: Mapped[str]
#     user_pk: Mapped[int] = mapped_column(
#         ForeignKey('my_app.user.pk')
#     )
#
#     user: Mapped['User'] = relationship(
#         back_populates='orders'
#     )
#     order_items: Mapped[list['OrderItem']] = relationship()
#
#     def __repr__(self) -> str:
#         return f'Order(pk={self.pk!r}, number={self.number!r})'
#
#
# class OrderItem(Base):
#     __tablename__ = 'my_app.order_item'
#
#     pk: Mapped[int] = mapped_column(
#         primary_key=True
#     )
#     price: Mapped[Decimal] = mapped_column(
#         Numeric(
#             precision=5,
#             scale=2
#         )
#     )
#     order_pk: Mapped[int] = mapped_column(
#         ForeignKey('my_app.order.pk')
#     )
