'''
context in python refers an environment where we execute code. python handle this scenario
with help of with statement and context manager. Basically context manager is an object which
provide two dunder method __enter__ and __exit__ for entering and exit to the context.

we deal with file system in those scenario we open a file and if we forget to close a file there is a
chance to data leak so context will help here to close a file after it used.
There are two ways to write custom context managers.
'''

'''
method 1 using __enter__ and __exit__ dunder methods.
__enter__ denotes about the enter in the context.
__exit__ denotes about the exit out of context.
if there are any exceptions came in the context then exec_type, exec_val and exec_tb(trace_back)
will come.
'''


class CustomContextManager:

    def __enter__(self):
        print("Entering into context.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting from context..")
        if exc_type:
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_val}")
            return False
        return True


with CustomContextManager() as manager:
    print("Inside context")


# method 2 using contextlib


from contextlib import contextmanager


@contextmanager
def custom_context_manager():
    print("Entering the context1..")
    try:
        # code before yielding acts like __enter__ method.
        yield
        # code after yielding acts like __exit__ method.
    finally:
        print("Executing the context1..")


with custom_context_manager():
    print("Inside the context block1.")

