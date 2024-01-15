def add_number(a, b, *args):
    add_number = a + b
    for element in args:
        add_number += element
    return add_number


print(add_number(3, 4, 5, 6, 7))

def read_element(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
read_element(name='ashish', age=23)