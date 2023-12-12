class Employee:

    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"The name of employee is {self.name}")


class Manager(Employee):

    def __init__(self, name):
        super().__init__(name)


    def get_salary(self):
        print(f"The salary of manager is very high.")


m = Manager('Ashish')
m.get_salary()
m.info()


