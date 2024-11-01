import pickle


personal_details = {'name': 'Ashish', 'age': 23, 'dob': '20-12-1223'}


with open('pickle.dump', 'wb') as file:
    pickle.dump(personal_details, file)


with open('pickle.dump', 'rb') as file:
    print(pickle.load(file))