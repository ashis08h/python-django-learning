a_string = "ashish"
print(a_string.find('h'))
print(a_string.rfind('h'))

new_string = a_string.replace('h', '')
print(new_string)
print(a_string)

new_index = a_string.index('h')
r_index = a_string.rindex('h')
print(new_index)
print(r_index)