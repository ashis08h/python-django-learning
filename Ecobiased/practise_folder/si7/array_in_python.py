from array import array
int_array = array('i', [1, 2, 3, 4])
print('int_array', int_array)
print('type', type(int_array))

float_array = array('d', [1.2, 2.3, 3.4, 4.5])
print('float_array', float_array)
print('type', type(float_array))

string_array = array('u', 'ashish')
print('string_array', string_array)
print('type', type(string_array))

boolean_array = array('b', [True, False])
print('boolean_array', boolean_array)
print('type', type(boolean_array))

print(int_array[1:2])
