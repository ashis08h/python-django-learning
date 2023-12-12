class Employee:

    company_name = 'Rudra'

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"{self.name} work in {self.company_name}")

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name


emp1 = Employee('ashosk')
emp1.show()
emp1.change_company('ram')
emp1.show()
emp2 = Employee("rohan")
emp2.show()