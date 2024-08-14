class Employee:

    company_name = 'Rudra coresoft'

    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"My name is {self.name} and company name is {self.company_name}")

    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company


e1 = Employee('Ashish')
e1.info()
e1.change_company('Accenture')
e1.info()
