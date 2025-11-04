from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


# @app.get('/')
# def index():
#     return {'data': {'name': 'Ashish'}}
#
#
# @app.get('/about')
# def about():
#     return {'data': 'this is about page'}


@app.get('/')
def index():
    return {'data': 'blog_list'}


# @app.get('/blog')
# def blog_list_with_limit(limit, publish:bool):
#
#     # here limit and publish are called query parameter means in the url we can pass value after ? symbol.
#     # by default it consider string as type of any query parameter, we can change the type as we have changed
#     # for publish as bool.
#     if publish:
#         return {'data': f'{limit} published blogs from blog_list'}
#     else:
#         return {'data': f'{limit} blogs from blog list'}


@app.get('/blog')
def blog_list_with_limit(limit=10, publish:bool=True, sort:Optional[str]=None):
    # here limit and publish are called query parameters means in the url we can pass the value after ?
    # by default it consider string as type of any query parameter, we can change the type as we have changed
    # for publish as bool.
    if publish:
        return {'data': f'{limit} published blogs from blog list'}
    else:
        return {'data': f'{limit} blogs from blog list'}


# @app.get('/blog{id}')
# def show(id):
#     # fetch blog with id = id
#     return {'data': id}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    # here id is path parameter which is passed in the url after /value
    # fetch blog with id = id
    return {'data': id}


# @app.get('/blog/{id}/comments')
# def comments(id):
#     # fetch blog comment with id = id
#     return {'data': {'1', '2'}}


@app.get('/blog/{id}/comments')
def comments(id: int, limit=10):
    # fetch blog comment with id = id
    # fastapi is enough to know which one is query parameter and which one is path parameter
    # it will check if parameter which is used in the defination of path operation function is present in the path
    # or not
    return {'data': ['1', '2', limit]}


'''this path will give error Input should be a valid integer, unable to parse string as an integer,
 input unpublished
 because fastapi reads code one after one ie line by line 
 so it will start reading from top and goes to show method only and since unpublished is not integer
 so it return error message, it will not reach upto unpublished method only.
 to work them we need to move unpublished method before the show method.
'''
# @app.get('blog/unpublished')
# def unpublished():
#     return {'data': "Unpublished blogs"}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'blog has been created successfully with title as {blog.title} and body as {blog.body}.'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=9000)
