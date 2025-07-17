a_string = "Ashish"
print(a_string.find("h"))
print(a_string.rfind("h"))
print(a_string.find("m"))

new_string = a_string.replace("h", "m")
print("new_string", new_string)

new_index = a_string.index("h")
print("new_index", new_index)

new_right_index = a_string.rindex("h")
print("new_r_index", new_right_index)