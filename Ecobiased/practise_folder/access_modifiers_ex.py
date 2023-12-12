class Employee:

    def __init__(self):
        self.__name = 'Ashish'


e = Employee()
# print(e.__name) this will give error.
print(e._Employee__name) # In this way we can access the protected variables.