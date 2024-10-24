"""
context in python refers as an environment where we execute the python code.
we handle such scenario by with statement and context manager.

context manager is an object which provide two dunder method __enter__ and __exit__ for entering and exiting
to the context.

we deal with file system where we open a file and if we forget to close it then there is a chance to
data leak in such scenario context manager help up to close the file. We can create a custom context manager.
"""


class CustomContextManager:

    def __enter__(self):
        print("Entering to context.")
        return self

    def __exit__(self, exec_type, exec_val, exec_tb):
        print("Exiting from context.")
        if exec_type:
            print("exec_type", exec_type)
            print("exec_val", exec_val)
            return False
        return True


with CustomContextManager() as manager:
    print("Inside the context")


from contextlib import contextmanager


@contextmanager
def custom_context_manager():
    print("Entering in the context1")
    try:
        # code before yielding acts like __enter__ method.
        yield
        # code after yielding acts like __exit__ method.
    finally:
        print("Executing context1.")


with custom_context_manager():
    print("Inside the context1.")
