from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, oauth2
from sqlalchemy.orm import Session
from ..repository import blog


# router = APIRouter()
# We can bring all the tags wherever we have written in initialize of APIRouter
# we can add prefix of all the user inside apirouter initialization.
router = APIRouter(
    tags=['Blogs'],
    prefix='/blog'
)

get_db = database.get_db


# @app.post('/blog')
# def create(title, body):
#     return {'title': title, 'body': body}


# @app.get('/blog')
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
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


# @app.post('/blog', status_code=201)
# def create(request: schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def destroy(id: int, db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)


# @app.get('/blog/{id}', status_code = 200)
# def show(id, response: Response, db: Session = Depends(get_db)):
#     """
#     Without response model
#     :param id:
#     :param response:
#     :param db:
#     :return:
#     """
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'detail': f"blog with id {id} does not exist"}
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"blog with id {id} does not exist")
#     return blog

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    """
    with response model
    :param id:
    :param response:
    :param db:
    :return:
    """
    return blog.show(id, db)


@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)
