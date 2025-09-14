import pickle

a_dict = {'name': 'ashish', 'age': 12, 'dob': '30-12-100'}

with open('pickle.dump', 'wb') as file:
    pickle.dump(a_dict, file)

with open('pickle.dump', 'rb') as file:
    print(pickle.load(file))
