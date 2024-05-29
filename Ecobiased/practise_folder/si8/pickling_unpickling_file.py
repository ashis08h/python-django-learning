import pickle

a_dict = {'name':'ashish', 'age':23, 'dob': 20}

with open('data.pickle', 'wb') as file:
    pickle.dump(a_dict, file)


with open('data.pickle', 'rb') as file:
    result = pickle.load(file)
    print(result)
