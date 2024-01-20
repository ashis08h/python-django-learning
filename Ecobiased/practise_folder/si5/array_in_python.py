from array import array

# integer element array
integer_array = array('i', [1, 2, 3, 4])
print("integer_array", integer_array)

# float element array
float_array = array('d', [1.2, 3.4, 8.9])
print("float_array", float_array)

# string array
string_array = array('u', 'kumar')
print("string_array", string_array)

# boolean array
boolean_array = array('b', [True, False])
print("boolean_array", boolean_array)

print(integer_array[2])
print(integer_array[1:4:2] # here last 2 is step same as list.