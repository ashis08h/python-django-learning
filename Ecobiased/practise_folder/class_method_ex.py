class Employee:

    company_name = 'Rudra'

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"{self.name} works in {self.company_name}")

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name


c1 = Employee('Ashish')
c1.show()
c1.change_company('Accenture')
c1.show()
