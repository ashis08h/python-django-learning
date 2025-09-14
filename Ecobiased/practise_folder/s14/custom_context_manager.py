"""
context in python refers an environment where we execute the python code. we handle this scenario with
help of with statement and context manager.

context manager is an object which provide two dunder method __enter__ and __exit__ for entering and exiting
into context.

we deal with file based system when we open a file after work if we forget to close a file then there will be
data leak chance, so context manager helps here to close that file after work is done.

we can create a custom context manager.
"""


class CustomContextManager:

    def __enter__(self):
        print("entering into context manager.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exiting from context manager.")
        if exc_type:
            print(exc_val)
            print(exc_type)
            return False
        else:
            return True


with CustomContextManager() as manager:
    print("Inside context manager")


from contextlib import contextmanager


@contextmanager
def custom_context_manager():
    try:
        print("Before yield just like __enter__")
        yield
        print("After yield just like __exit__")
    finally:
        print("Executing context")


with custom_context_manager():
    print("Inside context1")


def fun():
    try:
        return 1
    finally:
        return 2


print(fun())