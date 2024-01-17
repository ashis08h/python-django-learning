def perform_operation(x, y, callback):
    result = callback(x, y)
    print(f"The result is {result}")


def add(x, y):
    return x+y


def multiply(x, y):
    return x*y


perform_operation(2, 4, add)
perform_operation(3, 5, multiply)
