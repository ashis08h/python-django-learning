from array import array

int_array = array("i", [1, 2, 3, 4])
print("type", type(int_array))
print("int_array", int_array)

decimal_array = array("d", [1.2, 2.3, 3.4])
print("type", type(decimal_array))
print("decimal_array", decimal_array)

string_array = array("u", 'Ashish')
print("type", type(string_array))
print("string_array", string_array)

boolean_array = array("b", [True, False, True, False, False])
print("type", type(boolean_array))
print("boolean_array", boolean_array)