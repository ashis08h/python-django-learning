# class Car:
#
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#
# class Suv(Car):
#
#     def __init__(self, brand, model):
#         super().__init__(brand, model)
#         self.car_type = "Suv"
#         print(f"I am from {self.car_type}")
#         print("model", self.model)
#         print("brand", self.brand)
#
#
# class Sedan(Car):
#
#     def __init__(self, brand, model):
#         super().__init__(brand, model)
#         self.car_type = "Sedan"
#         print(f"I am from {self.car_type}")
#         print("model", self.model)
#         print("brand", self.brand)
#
#
# class FactoryClass:
#
#     def create_object(self, brand, model, car_type):
#
#         if car_type == 'Suv':
#             Suv(brand, model)
#         elif car_type == 'Sedan':
#             Sedan(brand, model)
#         else:
#             raise ValueError
#
#
# fc = FactoryClass()
# fc.create_object('Toyota', 'mod-123', 'Suv')
# fc.create_object('Etios', 'mod-345', 'Sedan')


# input_list = ["asd","qwe","zxc"]
#
# result = list(map(lambda x: x[::-1], input_list))
# main_result = result[::-1]
# print(main_result)
#
# input_list = [1, 2, 3, 4, 5, 6]
#
#
# def square_num(num):
#     return num ** 2
#
#
# def is_even(num):
#     if (num % 2):
#         return False
#     else:
#         return True
#
# is_even = list(filter(is_even, input_list))
# print("is_even", is_even)
#
# square_numbers = list(map(square_num, input_list))
# print("square_numbers", square_numbers)

# guest_list = [1, 2, 3, 'v1', 'v2', ('v1', 'v2'), [4, 5], 'v1']
# main_list = []
# for item in guest_list:
#     if isinstance(item, tuple):
#         main_list.extend(item)
#     elif isinstance(item, list):
#         main_list.extend(item)
#     else:
#         main_list.append(item)
#
# print(main_list)
# first_row = []
# second_row = []
# for item in main_list:
#     if isinstance(item, str):
#         first_row.append(item)
#     else:
#         second_row.append(item)
# main_row = [first_row, second_row]
# print(main_row)


# Brand
# id, pk - 1
# brand_name - 'Apple'
#
# Model
# id - pk - 1
# model_number - 'Mod123'
#
# Item
# id- pk- 1
# itemcode - 'Iem-1234'
# brand_id = fk(with brand)
# model_id = fk(with_model)
#
#
# Order -
# id - pk - 1
# order_id - 'ord-123'
# item_ids = manytoonefield
#
# payment -
# id, 1
# payment_id, 'py-11'
# payment_mode - 'cash/card'
# utr_no = optional
# order_id fk
#
#
# my
# mummy
# Mumbai
# Bihar
# Maharastra
#
#
# select * from city where city_name ilike '%val%'
#






