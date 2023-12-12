class Employee:

    def __init__(self):
        self.name = "Ashish"
        self.__age = 23
        self.__dob = '23456'


e = Employee()
print(e.name)
#print(e.__age)
print(e._Employee__age)
print(e._Employee__dob)