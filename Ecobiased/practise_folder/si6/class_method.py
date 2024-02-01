class Employee:

    company_name = 'Rudra coresoft technologies pvt ltd'

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company

    def info(self):
        return f"My name is {self.name} and my company is {self.company_name}"


e = Employee('Ashish')
print(e.info())
e.change_company('Accenture')
print(e.info())
