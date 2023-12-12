class Employee:

    company_name = 'Rudra' # class variable

    def __init__(self, n):
        self.name = n # instance variable
        self.raise_amt = '0.2' # instance variable

    def show_details(self):
        print(f"{self.name} has raise {self.raise_amt} and his company is {self.company_name}")


emp1 = Employee('ashish')
emp1.company_name = 'Google'
emp1.show_details()
emp2 = Employee('rohan')
emp2.company_name = 'Nestle'
emp2.show_details()
Employee.company_name = 'Facebook'
emp1.show_details()
emp2.show_details()
emp3 = Employee("rishika")
emp3.show_details()