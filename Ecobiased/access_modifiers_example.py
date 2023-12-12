# Public default one.
class Employee:

    def __init__(self):
        self.name = 'Ashish'


e = Employee()
print(e.name)


# Private one.
class Employee1:

    def __init__(self):
        self.__name = 'Ashish1'


e1 = Employee1()
#print(e1.__name) # It will give error.
print(e1._Employee1__name) # we can access it by name mangeling.


# Protected one.
class Employee2:

    def __init__(self):
        self._name = 'Ashish2'


e2 = Employee2()
print(e2._name)

