from fastapi import APIRouter, Depends
from .. import database, schemas
from sqlalchemy.orm import Session
from .. repository import user


# we can bring all the tags wherever we have written in initialize of APIRouter
# we can add prefix of all the user inside APIRouter initialization.

router = APIRouter(
    tags=['Users'],
    prefix='/user'
)


get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
    return user.show(id, db)