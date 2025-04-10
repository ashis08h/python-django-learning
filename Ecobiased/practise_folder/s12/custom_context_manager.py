"""
context in python refer as an environment where we execute the python code. We handle these
scenario with help of with statement and context manager.

context manager is an object which provide two dunder method __enter__ and __exit__ for entering
and exiting to the context.

we deal with file based system where open a file and if we forget to close that file then there is
a chance to data leak so here context manager help here to close the file after work completes.
We can create a custom context manager.
"""

from contextlib import contextmanager


class CustomContextManager:

    def __enter__(self):
        print("Entering into custom context manager.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting from custom context manager.")
        if exc_type:
            print(exc_type)
            print(exc_val)
            return False
        else:
            return True


with CustomContextManager() as manager:
    print("Inside the customcontextmanager.")


@contextmanager
def custom_context_manager():
    try:
        print("Before yield just like __enter__ method.")
        yield
        print("After yield just like __exit__ method.")
    finally:
        print("Executing context1")


with custom_context_manager():
    print("Inside context1.")


