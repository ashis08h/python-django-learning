class Employee:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show_details(self):
        print(f"The employee {self.id} name is {self.name}")


e1 = Employee(4, 'Ashish')
e1.show_details()


class Programmer(Employee):

    def show_language(self):
        print("The default language is python.")


p1 = Programmer(3, 'Rishika')
p1.show_details()
p1.show_language()