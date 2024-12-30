def to_lower(func):
    def wrapper():
        result = func()
        return result.lower()
    return wrapper


@to_lower
def text_hello():
    return 'Hello World'


print(text_hello())


num = 4567

str_1 = str(num)
rev_str = str_1[::-1]
print(rev_str)