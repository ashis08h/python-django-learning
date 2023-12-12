class Person:
    name = 'Ashish'
    designation = 'Software developer'
    networth = 10

    def info(self):
        print(f"{self.name} is a {self.designation} and his networth is {self.networth}")


person1 = Person()
person1.name = "rishika"
person1.designation = "housewife"
person1.networth = 5
person1.info()
person2 = Person()
person2.info()