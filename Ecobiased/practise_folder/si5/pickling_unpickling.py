import pickle

person_info = {'name': 'ashish', 'age': 23, 'male': 'sex'}

with open('data1.pickle', 'wb') as file:
    pickle.dump(person_info, file)

with open('data1.pickle', 'rb') as file:
    result = pickle.load(file)
    print('result', result)