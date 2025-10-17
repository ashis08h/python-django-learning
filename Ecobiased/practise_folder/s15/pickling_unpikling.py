import pickle

a_dict = {'name': 'Ashish', 'age': 12, 'dob': '30-12-1995'}

with open('pickle.dump', 'wb') as file:
    pickle.dump(a_dict, file)

with open('pickle.dump', 'rb') as file:
    print(pickle.load(file))
