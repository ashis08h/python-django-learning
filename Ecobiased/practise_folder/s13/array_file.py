from array import array


int_array = array("i", [1, 2, 3, 4])
print("int_array", int_array)
print(type(int_array))

decimal_array = array("d", [1.2, 2.3, 3.4])
print("decimal_Array", decimal_array)
print(type(decimal_array))

string_array = array("u", "Ashish")
print("string_array", string_array)
print(type(string_array))

boolean_array = array("b", [True, False, True, False, False])
print("boolean_array", boolean_array)
print(type(boolean_array))