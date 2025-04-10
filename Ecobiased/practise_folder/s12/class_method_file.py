class Person:

    copmany_name = "Rudra coresoft technology pvt ltd"

    def __init__(self, name):
        self.name = name

    def info(self):
        return f"My name is {self.name} and my company name is {self.copmany_name}"

    @classmethod
    def change_company(cls, new_company):
        cls.copmany_name = new_company


p = Person("Ashish")
print(p.info())
p.change_company('XYZ')
print(p.info())
