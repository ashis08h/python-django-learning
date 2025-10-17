"""
context refers an envireonment in python where we execute our python code. We handle a situation with help of
with statement and context manager.

context manager is an object which provide two dunder method __enter__ and __exit__ to entering and exiting into
the context.

when we deal with file base system, we open a file and do some work, if we forget to close the file after work
done then there is a chance of data leak. here context manager help to close the file after work done.

we can create a custom context manager also.
"""


class CustomContextManager:

    def __enter__(self):
        print("entering into context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exiting from context")
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
        print("executing context")


with custom_context_manager():
    print("inside context1")


def fun():
    try:
        print("come in 1")
        return 1
    finally:
        return 2


print(fun())