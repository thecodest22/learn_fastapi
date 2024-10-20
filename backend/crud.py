from sqlalchemy import select
from sqlalchemy.orm import Session

import models, schemas


def get_users(db: Session):
    stmt = select(models.User)
    result = db.execute(stmt)
    r = result.all()
    return r


def create_user(db: Session, user: schemas.UserCreateModel):
    user = user
    print(user)
    db_user = models.User()
