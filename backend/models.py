from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class User(Base):
    __tablename__ = 'my_app_user'

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
#     __tablename__ = 'my_app_orders'
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
#     __tablename__ = 'my_app_order_item'
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
