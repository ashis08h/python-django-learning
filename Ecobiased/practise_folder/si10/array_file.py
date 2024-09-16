from array import array

int_array = array('i', [1, 2, 3, 4, 5])
print('int_array', int_array)
print('type_of_array', type(int_array))

decimal_array = array('d', [1.2, 2.3, 4.5])
print('decimal_array', decimal_array)
print('type_of_array', type(decimal_array))

string_array = array('u', 'ashish')
print('string_array', string_array)
print('type_of_array', type(string_array))

boolean_array = array('b', [True, False, False, True])
print('boolean_array', boolean_array)
print('type', type(boolean_array))