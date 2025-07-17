"""
context in python refers an environment where we execute the python code. we handle these scenario
with help of context manager and with statement.

context manager is an object which provides two dunder method __enter__ and __exit__ for entering and existing the
into the context.

we deal with file based system where we open a file, after the work if we forget to close a file then there will be
data leak chance, so context manager helps here to close that file after work is done.

We can create a custom context manager.
"""

from contextlib import contextmanager


class CustomContextManager:

    def __enter__(self):
        print("entering into the context manager.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exiting from custom manager")
        if exc_type:
            print(exc_type)
            print(exc_val)
            return False
        else:
            return True


with CustomContextManager() as manager:
    print("Inside context manager.")


@contextmanager
def custom_context_manager():
    try:
        print("Before yield just like __enter__ method")
        yield
        print("After yield just like __exit__ method")
    finally:
        print("Executing context")


with custom_context_manager():
    print("Inside context1")




