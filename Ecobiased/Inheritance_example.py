class Employee:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show_details(self):
        print(f"The name of employee {self.id} is {self.name}.")


class Programmer(Employee):

    def show_language(self):
        print(f"The basic language is python")


e = Employee(1, "ashish")
e.show_details()

p = Programmer(2, 'Rishika')
p.show_details()
p.show_language()
