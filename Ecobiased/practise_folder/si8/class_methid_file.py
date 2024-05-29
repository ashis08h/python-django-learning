class Employee:

    company_name = 'Rudra coresoft technology'

    def __init__(self, name):
        self.name = name

    def info(self):
        return f'My name is {self.name} and company name is {self.company_name}'

    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company


e = Employee('Ashish')
print(e.info())

e.change_company('Accenture')
print(e.info())