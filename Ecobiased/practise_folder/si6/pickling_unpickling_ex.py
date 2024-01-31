import pickle

a_dict = {'name': 'Ashish', 'age':29, 'male': 'sex'}

with open('data.pickle', 'wb') as file:
    pickle.dump(a_dict, file)

with open('data.pickle', 'rb') as file:
    result = pickle.load(file)
    print("result", result)