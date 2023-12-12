class Math:

    def __init__(self, num):
        self.num = num

    @staticmethod
    def add(a,b):
        return a+b


a = Math(5)
print(a.num)
print(Math.add(4,8)) # We can call static method by classname .method name also.
print(a.add(4,5))