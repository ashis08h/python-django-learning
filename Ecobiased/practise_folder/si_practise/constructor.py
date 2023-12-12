class Person:

    def __init__(self, name, age):
        print("called from constructor.")
        self.name = name
        self.age = age

    def info(self):
        print(f"My name is {self.name} and my age is {self.age}")


person_obj = Person('Ashish', 40)
print(person_obj.name)
print(person_obj.age)