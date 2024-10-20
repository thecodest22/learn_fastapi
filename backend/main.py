import pathlib
from decimal import Decimal
from enum import Enum
from typing import Union

from fastapi import Depends, FastAPI, Path, Query
from pydantic import BaseModel
from sqlalchemy.orm import Session

import crud, database, schemas

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Простейшая вьюха. Никаких аннотаций нет, поэтому фастапи слушает сегмент пути
# как строку.
# @app.get('/echo/{value}')
# def get_item(value):
#     return {'Вы ввели в адресе вот это: ': value}
# # -----------------------------------------------------------------------------
#
# # Добавили простую аннотацию типов. Появится в документации и будет валидация.
# @app.get('/my_items/{item_pk}')
# def get_my_item(item_pk: int):
#     return {'item_pk': item_pk}
# # -----------------------------------------------------------------------------
#
# # В качестве допустимых значений параметра пути можно использовать перечисления
# class AllowedPathValues(str, Enum):
#     foo = 'foo'
#     bar = 'bar'
#     spam = 'baz'
#
#
# @app.get('/some_path/{path_value}')
# async def get_some_response(path_value: AllowedPathValues):
#     # Когда фастапи парсит реквест, то приводит значение к тому типу,
#     # что указан в аннотации, поэтому "path_value" уже будет нужного класса
#
#     if path_value is AllowedPathValues.foo:
#         # Перед респонсом из этого экземпляра будет создана строка.
#         return {'Path value is foo': path_value}
#
#     if path_value.value == 'bar':
#         return {'Path value is bar': path_value.value}
#
#     return {'Path value is baz': path_value}
# # -----------------------------------------------------------------------------
#
# # Можно также объявлять конвертеры пути, например:
# @app.get('/itms/{itm_id:int}')
# def get_itm(itm_id):
#     # Тогда сегмент будет преобразован в инт. При попытке передать строку - 404
#     return {'item_id': itm_id}
#
#
# @app.get('/files/{file_path:path}')
# async def get_file(file_path: str):
#     return {'file_path': file_path}
#
#
# @app.get('/my_files/{file_path:path}')
# async def get_my_file(file_path: pathlib.Path):
#     return {'file_path': file_path}
# # -----------------------------------------------------------------------------
# #
# # Если в функции объявить параметры, не относящиеся к переменным пути, они
# # будут восприниматься как квери-параметры.
# db_users = [{'id': 1, 'name': 'vasya'},
#             {'id': 2, 'name': 'petya'},
#             {'id': 3, 'name': 'kolya'},
#             {'id': 4, 'name': 'vasya'},
#             {'id': 5, 'name': 'igor'}]
#
# # При такой аннотации квери-параметр станет обязательным!
# #
# # async def get_user(user_id: int, users_name: str):
# #
# # Поэтому объявляем со значением по умолчанию, в т.ч. None.
#
# @app.get('/my_users/{user_id}')
# def get_user(user_id: int, user_name: str | None = None):
#     return [user for user in db_users
#             if user['id'] == user_id
#             and (user_name is None or user['name'] == user_name)]
# # -----------------------------------------------------------------------------
# #
# # Для объявления и валидации тела запроса, нужна модель pydantic.
# # Будет проведена проверка и преобразование типов. Теперь параметр функции надо
# # аннотировать этой моделью
# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None  # Необязательный параметр тела
#     price: Decimal
#     tax: Union[float, None] = None
#
#
# @app.post('/items-1/')
# async def create_item(item: Item):
#     return item
# # -----------------------------------------------------------------------------
#
# # В параметрах функции можно объявить и часть пути, и квери-параметр, и тело.
# # Фастапи интерпретирует:
# #   - параметр, имя которого совпадает с именем в пути, как параметр пути;
# #   - параметр, имени которого нет в пути, как квери-параметр;
# #   - параметр, аннотированный моделью pydantic, как тело запроса.
# @app.put("/items-1/{item_id}")
# async def update_item(item_id: int, item: Item, q: Union[str, None] = None):
#     result = {"item_id": item_id, **item.model_dump()}
#     if q:
#         result.update({"q": q})
#     return result


@app.get('/users/', response_model=list[schemas.UserListRetrieveModel])
def get_users(db: Session = Depends(get_db)):
    result = crud.get_users(db)
    return result