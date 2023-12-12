class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_str(cls, frm_str):
        return cls(frm_str.split('_')[0], frm_str.split('_')[1])


e = Employee('Ashish', 21)
print(e.name)
print(e.age)
e1 = Employee.from_str("Ashish_21")
print(e1.name)
print(e1.age)
