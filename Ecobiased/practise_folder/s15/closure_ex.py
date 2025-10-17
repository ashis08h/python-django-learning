def outer(x):

    def inner(y):
        return x + y
    return inner


add_5 = outer(5)

print(add_5(10))

# Here inner is a closure because it remember the outer variable x.