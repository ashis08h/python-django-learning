a_string = "ashish"
print(a_string.find('h'))
print(a_string.rfind('h'))

new_str = a_string.replace("h", "")
print("new_str", new_str)
print("a_string", a_string)

new_index = a_string.index('h')
print("new_index", new_index)

new_index_from_right = a_string.rindex('h')
print("new_r_index", new_index_from_right)