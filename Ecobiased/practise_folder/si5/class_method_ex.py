class Employee:

    company_name = "Rudra coresoft"

    def __init__(self):
        self.name = 'Ashish'

    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company

    def info(self):
        print(f"My name is {self.name} and my company name is {self.company_name}")


e = Employee()
e.info()
e.change_company('Accenture')
e.info()
