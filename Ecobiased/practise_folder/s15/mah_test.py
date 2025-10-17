# def add_hi(func):
#     def wrapper():
#         result = func()
#         return "Hi " + result
#     return wrapper
#
#
# @add_hi
# def say_hello():
#     return "Ashish"
#
#
# print(say_hello())

# list1 = [1,2,[3,4],[5,6,[7,8]]]
#
#
# def flattened_list(input_list):
#     result_list = []
#     for item in input_list:
#         if isinstance(item, list):
#             result_list.extend(flattened_list(item))
#         else:
#             result_list.append(item)
#     return result_list
#
#
# print(flattened_list(list1))


# input = 'aaabbbbcca'
# output = '3a4b2c'
#
# temp_list = []
# result = ""
#
# for char in input:
#     if char not in temp_list:
#         temp_list.append(char)
#         result = result + str(input.count(char)) + char
#
# print(result)




