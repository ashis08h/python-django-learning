from ..hashing import Hash
from .. import schemas, models
from fastapi import HTTPException, status
from sqlalchemy.orm import Session


def create(request: schemas.User, db:Session):
    password = request.password[:72]
    hashed_password = Hash().bcrypt(password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, \
                            detail=f"User with the id {id} is not Available.")
    return user