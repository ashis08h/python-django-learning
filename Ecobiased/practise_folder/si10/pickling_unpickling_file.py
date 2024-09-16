import pickle


personal_details = {'name': 'Ashish', 'age': 29, 'dob': '30-12-1995'}

with open('pickle.dump', 'wb') as file:
    pickle.dump(personal_details, file)


with open('pickle.dump', 'rb') as file:
    print(pickle.load(file))