class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_str(cls, str_data):
        return cls(str_data.split("_")[0], str_data.split("_")[1])


e = Employee('Ashish', 10)
print(e.name)
print(e.salary)

e1 = Employee.from_str("raj_30")
print(e1.name)
print(e1.salary)