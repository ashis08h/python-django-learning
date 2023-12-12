# Example of list comprehension.

old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = [item**2 for item in old_list if item]
print(new_list)

# Example of dict comprehension

fruits_list = ['Mango', 'Banana', 'Apple', 'Guava']
new_dict = {item: len(item) for item in fruits_list if item}
print(new_dict)