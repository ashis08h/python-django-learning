class Myclass:

    def __init__(self, v):
        self.value = v

    def show(self):
        print(f"The value is {self.value}")

    @property
    def ten_value(self):
        return self.value * 10

    @ten_value.setter
    def ten_value(self, new_value):
        self.value = new_value/10


c1 = Myclass(10)
c1.show()
print(c1.ten_value)
c1.ten_value = 67
c1.show()
print(c1.ten_value)


