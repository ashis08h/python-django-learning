import pickle

data = {'name': 'ashish', 'age': 29, 'address': 'munger'}

with open('data.pickle', 'wb') as file:
    pickle.dump(data, file)

original_obj = None
with open('data.pickle', 'rb') as file:
    original_obj = pickle.load(file)
print(original_obj)