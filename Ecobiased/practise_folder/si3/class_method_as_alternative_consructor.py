class MyClass:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_str(cls, name_age):
        return cls(name_age.split("_")[0], name_age.split("_")[1])


my_class = MyClass('Ashish', 23)
print(my_class.name)
print(my_class.age)


my_class1 = MyClass.from_str("Ashish_23")
print(my_class1.name)
print(my_class1.age)