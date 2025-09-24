from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


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
# def blog_list_with_limit(limit, published:bool):
#     # here limit and published is called query parameter means in url we can pass value with ? symbol.
#     # by default it consider string as type of any query parameter we can change the type as we have changed
#     # for published as bool.
#     if published:
#         return {'data': f'{limit} published blogs from blog_list'}
#     else:
#         return {'data': f'{limit} blogs from blog_list'}


@app.get('/blog')
def blog_list_with_limit(limit=10, published:bool=True, sort:Optional[str]=None):
    # here limit and published is called query parameter means in url we can pass value with ? symbol.
    # by default it consider string as type of any query parameter we can change the type as we have changed
    # for published as bool.
    if published:
        return {'data': f'{limit} published blogs from blog_list'}
    else:
        return {'data': f'{limit} blogs from blog_list'}


# @app.get('/blog/{id}')
# def show(id):
#     # fetch blog with id = id
#     return {'data': id}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': "Unpublished blogs"}


@app.get('/blog/{id}')
def show(id: int):
    # here id is called path parameter which is passed in the url as /value
    # fetch blog with id = id
    return {'data': id}


# @app.get('/blog/{id}/comments')
# def comments(id):
#     # fetch blog comment with id = id
#     return {'data': {'1', '2'}}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    # fetch blog comment with id = id
    # fastapi is enough smart to know which one is path parameter and which one is query parameter
    # It will check if parameter which is used in the definition of path operation function is present in the
    # path or not.
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


# code to change the port from 8000 to 9000

# use below code and in the terminal you can run
# python main.py

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=9000)