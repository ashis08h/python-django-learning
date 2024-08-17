import pickle

a_dict = {'name': 'ashish', 'age': 20, 'dob': '23-02-2000'}

with open('data.pickle', 'wb') as file:
    pickle.dump(a_dict, file)


with open('data.pickle', 'rb') as file:
    result = pickle.load(file)
    print("result", result)
