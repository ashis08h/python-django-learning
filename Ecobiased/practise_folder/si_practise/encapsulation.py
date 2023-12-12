class Person:

    def __init__(self, public_var, _protected_var, __private_var):
        self.public_var = public_var
        self._protected_var = _protected_var
        self.__private_var = __private_var

    def get_private_var(self):
        return self.__private_var

    def set_private_var(self, new_var):
        self.__private_var = new_var


p1 = Person("ashish", "annu", "rishika")
print(p1.public_var)
print(p1._protected_var)
#print(p1.__private_var)
print(p1.get_private_var())
p1.set_private_var('jacky')
print(p1.get_private_var())