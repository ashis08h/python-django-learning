a_string = "ashish"
print(a_string.find('h'))
print(a_string.rfind('h'))

new_str = a_string.replace("h", "")
print("new_str", new_str)
print("a_str", a_string)

new_index = a_string.index("h")
print("new_index", new_index)

ren_rindex = a_string.rindex("h")
print("newrindex", ren_rindex)