class Person:

    company_name = "Rudra coresoft"

    def __init__(self, name):
        self.name = name

    def info(self):
        return f"My name is {self.name} and my company is {self.company_name}"

    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company


p = Person("Ashish")
print(p.info())

p.change_company("Accenture")
print(p.info())