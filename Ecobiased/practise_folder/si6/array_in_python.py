from array import array

integer_array = array('i', [1, 2, 3, 4])
print(integer_array)

float_array = array('d', [1.3, 3.4, 4.5])
print(float_array)

string_array = array('u', 'ashish')
print(string_array)

boolean_array = array('b', [True, False])
print(boolean_array)

print(integer_array[2])
print(integer_array[1:4:2])