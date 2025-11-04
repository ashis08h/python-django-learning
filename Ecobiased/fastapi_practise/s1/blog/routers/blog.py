from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import database, schemas, models
from sqlalchemy.orm import Session
from ..repository import blog
from fastapi import FastAPI
from .. import oauth2



# we can bring all the tags wherever we have written in initialize of APIRouter
# we can add prefix of all the user inside APIRouter intialization
router = APIRouter(
    tags=['Blogs'],
    prefix='/blog'
)

#app = FastAPI()

get_db = database.get_db


# @router.post('/blog')
# def create(title, body):
#     return {'title': title, 'body': body}


# @router.get('/blog')
# def get(db: Session = Depends(get_db)):
#     """
#     without response model
#     :param db:
#     :return:
#     """
#     blogs = db.query(models.Blog).all()
#     return blogs


# without protection with token
# @router.get('/', response_model=List[schemas.ShowBlog])
# def all(db: Session = Depends(get_db)):
#     return blog.get_all(db)


@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('/blog', status_code=201)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
