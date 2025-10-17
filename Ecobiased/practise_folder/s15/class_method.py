class Person:

    company_name = "Rudra coresoft"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"My name is {self.name} and age is {self.age} and my company is {self.company_name}"

    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company


p = Person("Ashish", 34)
print(p.info())

p.change_company('Accenture')
print(p.info())
