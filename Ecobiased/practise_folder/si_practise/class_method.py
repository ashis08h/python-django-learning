class Person:

    company_name = "Rudra coresoft pvt ltd."

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and my age is {self.age} my company name is {self.company_name}")

    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company


p1 = Person('Ashish', 23)
p1.show()
p1.change_company('accenture')
p1.show()
