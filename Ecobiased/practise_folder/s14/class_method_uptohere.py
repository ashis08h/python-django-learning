class Person:

    company_name = "Rudra coresoft"

    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"My name is {self.name} and company name is {self.company_name}")

    def change_company(cls, new_company):
        cls.company_name = new_company


p = Person("Ashish")
p.info()
p.change_company("Accenture")
p.info()