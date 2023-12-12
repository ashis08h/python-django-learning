import pickle

# a_dict = {'name': 'ashish', 'age': 29, 'sex': 'male'}
#
# with open('a_data.pickle', 'wb') as file:
#     pickle.dump(a_dict, file)

with open('a_data.pickle', 'rb') as file:
    load_data = pickle.load(file)
print("load_data", load_data)
