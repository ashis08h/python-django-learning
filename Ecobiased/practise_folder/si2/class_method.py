class Person:

    company = 'Accenture'

    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Hi My name is {self.name} and my company is {self.company}")

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name


p = Person('Ashish')
p.info()
p.change_company('Rudra')
p.info()