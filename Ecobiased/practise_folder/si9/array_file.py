from array import array

int_array = array('i', [1, 2, 3, 4])
print('int_array', int_array)
print('type', type(int_array))

descimal_array = array('d', [1.2, 3.4, 4.0, 5.5])
print('decimal_array', descimal_array)
print('type', type(descimal_array))

string_array = array('u', 'name')
print('string_array', string_array)
print('type', type(string_array))

boolean_array = array('b', [True, False, True, False, False])
print('boolean_array', boolean_array)
print('type', type(boolean_array))
