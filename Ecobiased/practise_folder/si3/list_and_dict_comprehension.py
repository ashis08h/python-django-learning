a_list = [1, 3, 4, 5, 6, 7]

new_list = [item**2 for item in a_list if item]
print("new_list", new_list)

fruits = ['Mango', 'Litchi', 'Banana', 'Apple', 'Guava']
new_dict = {item: len(item) for item in fruits if item}
print("new_dict", new_dict)