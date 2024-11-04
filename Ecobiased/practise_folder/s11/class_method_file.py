class Person:

    company_name = 'Rudra'

    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"My name is {self.name} and my company name is {self.company_name}")

    @classmethod
    def change_company(cls, new_copmany):
        cls.company_name = new_copmany


p = Person('Ashish')
p.info()
p.change_company('Accenture')
p.info()
