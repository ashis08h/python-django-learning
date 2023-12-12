a_list = [1, 2, 3, 4, 5, 6]

b_list = [item**2 for item in a_list if item]
print("b_list", b_list)

a_list1 = ['ash', 'boyed', 'sirjis', 'ashish kumar']
b_dict = {item: len(item) for item in a_list1 if item}
print("b_dict", b_dict)