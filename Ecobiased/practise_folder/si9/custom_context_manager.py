from contextlib import contextmanager


class CustomContextManager:

    def __enter__(self):
        print("Entering into context..")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")
        if exc_type:
            print(f"exec val is {exc_val}")
            print(f"exec tb is {exc_tb}")
            return False
        return True


with CustomContextManager() as manager:
    print("Inside context manager.")


@contextmanager
def custom_context_manager():
    print('Entering context 1..')
    try:
        # code before yielding acts like __enter__ method.
        yield
        # code after yielding acts like __exit__ method.
    finally:
        print("Executing the context.")


with custom_context_manager():
    print("Inside context.")