class Employee:

    company_name = 'Rudra coresoft'

    def __init__(self, name):
        self.name = name

    def show(self):
        return f"My name is {self.name} and my company name is {self.company_name}"

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name


e = Employee('Ashish')
print(e.show())
e.change_company('Accenture')
print(e.show())