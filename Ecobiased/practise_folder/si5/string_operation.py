a_string = "ashish"

print(a_string.find('h')) # if it print -1 means it is not there.
print(a_string.find('k'))

# to remove a text in a string

new_string = a_string.replace('h', '')
print(new_string)

# get the index of a string

index = a_string.index('h')
print("index", index)