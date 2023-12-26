import pickle

person_info_dict = {'name': 'Ashish', 'Age': 30, 'Sex': 'Male'}

with open('data1.pickle', 'wb') as file:
    pickle.dump(person_info_dict, file)

with open('data1.pickle', 'rb') as file:
    result = pickle.load(file)
    print(result)