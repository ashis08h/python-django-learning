class Employee:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show(self):
        print(f"The id is {self.id} and the name is {self.name}")


class Programmer(Employee):

    def show_language(self):
        print(f"The default language is Python.")


p = Programmer(1, 'ashish')
p.show()
p.show_language()