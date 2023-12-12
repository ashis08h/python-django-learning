class Person:
    name = 'Ashish'
    designation = 'Software Engineer'
    networth = 10

    def info(self):
        print(f"{self.name} is a {self.designation} and his networth is {self.networth}.")


a = Person()
a.info()
a.name = 'Rishika'
a.designation = 'House wife'
a.networth = 100

a.info()