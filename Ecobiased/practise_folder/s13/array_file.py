from array import array


integer_array = array('i', [1, 2, 3, 4])
print("integer_array", integer_array)
print("type", type(integer_array))

decimal_array = array('d', [1.1, 2.2, 3.3])
print("decimal_array", decimal_array)
print("type", type(decimal_array))

string_array = array('u', 'Ashish')
print("string_array", string_array)
print("type", type(string_array))

bolean_array = array('b', [True, False, True])
print("bolean_array", bolean_array)
print("type", type(bolean_array))

print(bolean_array[1])