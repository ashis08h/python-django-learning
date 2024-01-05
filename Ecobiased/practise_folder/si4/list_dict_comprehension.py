a_list = [1, 2, 3, 4, 5, 6]

square_list = [item**2 for item in a_list if item]
print("square_list", square_list)

b_list = ["as", "ash", "ashi", 'ashis', "ashish"]

a_dict = {key: len(key) for key in b_list if key}
print(a_dict)