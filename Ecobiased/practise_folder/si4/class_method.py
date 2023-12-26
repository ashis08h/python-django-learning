class Employee:

    company_name = "Rudra coresoft technologies pvt ltd."

    def __init__(self):
        self.name = 'Ashish'

    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company

    def show_info(self):
        return f"My name is {self.name} and my company name is {self.company_name}"


e1 = Employee()
print(e1.show_info())
e1.change_company('Accenture')
print(e1.show_info())