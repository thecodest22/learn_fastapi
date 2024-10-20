from typing_extensions import Annotated

from pydantic import BaseModel, ConfigDict, StringConstraints


# Пробуем получить из БД юзера.
class UserBaseModel(BaseModel):
    first_name: Annotated[str, StringConstraints(max_length=30)]
    last_name: str | None


class UserCreateModel(UserBaseModel):
    pass


class UserListRetrieveModel(UserBaseModel):
    pk: int

    model_config = ConfigDict(from_attributes=True)
