import pickle

a_dict = {'name': 'Ashish', 'Age': 20, 'Sex': 'Male'}

with open('data1.pickle', 'wb') as file:
    pickle.dump(a_dict, file)

get_obj = None
with open('data1.pickle', 'rb') as file:
    get_obj = pickle.load(file)
print("get_obj", get_obj)