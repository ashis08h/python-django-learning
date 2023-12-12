class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_str(cls, string):
        return cls(string.split('-')[0], string.split('-')[1])


emp1 = Employee('ashish', 12000)
print(emp1.name)
print(emp1.salary)

emp2 = Employee.from_str('Rishika-20000')
print(emp2.name)
print(emp2.salary)