# list1 = [1, 2, 3, 4]
# tuple = (1, 2, 3, 4)
# set1 = {1, 2, 3}
# dict1 = {'name': 'ashish', 'age': 28}
#
# list1.append(5)
# list2 = [6, 7, 8]
# list1.extend(list2)
# print(list1)
#
# set2 = {3, 4, 5}
#
# common_element = set1 - set2
# print(common_element)
#
# print(dict1['name'])
#
# if 'salary' in dict1:
#     print(dict1['salary'])
# else:
#     print('NA')
# #
# # result = dict1['salary']
#
# str1 = "This # is # a # python # discussion."
#
# new_list = str1.split(' # ')
# print(new_list)
#
# new_str = " # ".join(new_list)
# print(new_str)
#
# #
# # We want to have odd numbers in the range 1 to 50, which is(are) the correct statement
# # (a) list(filter(lambda x: x%2, range(1,50)))
# # (b) [i for i in range(1,50) if i%2]
# # (c) [i for i in range(1,50) if x%2 !=0]
# # (d) list(range(1,51,2))
# #
# # Implement
# # the
# # function
# # below
# # so
# # that
# # a is positional
# # argument and b is a
# # keyword
# # argument
# # with a value of 5
#
#
# def add_two(a,b=5):
#     return a + b
#
#
# print(add_two(2))
#
#
# # use
# # function
# # annotation / typing
# # hints
#
# list1 = [1, 2, 4]
#
# def generate_element(list1):
#     for element in list1:
#         yield element
#
# print(generate_element(list1).__next__())
# print(generate_element(list1).__next__())
# print(generate_element(list1).__next__())
#
# # Correct
# # the
# # decorator
# # implementation
# # below
# # by
# # uncommenting
# # the
# # line(s)
# # necessary
#
#
# def OuterWrapper(func):
#     def decorator(*args, **kwargs):
#         print("Decorator started")
#         ## a = ["This is the most important line"]
#         func(*args, **kwargs)
#         print("Decorator ended")
#     return decorator
#
#
# @OuterWrapper
# def Square(x):
#     print(x ** 2)


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("I am in constructor.")

    def __str__(self):
        return f"{self.x}i, {self.y}j"

    def __add__(self, other):
        return Point(self.x + other.x, self.x + other.y)


p1 = Point(2, 5)
p2 = Point(3, 6)

print(p1 + p2)


# Square(5)