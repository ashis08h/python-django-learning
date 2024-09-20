class Person:

    def __init__(self, public_var, __private_var, _protected_var):
        self.public_var = public_var
        self._protected_var = _protected_var
        self.__private_var = __private_var

    def get_private_var(self):
        return self.__private_var

    def set_private_var(self, new_var):
        self.__private_var = new_var


p = Person('public', 'private', 'protected')
print("public_var", p.public_var)
print("protected_var", p._protected_var)
print(p.get_private_var())
p.set_private_var('set_private')
print(p.get_private_var())