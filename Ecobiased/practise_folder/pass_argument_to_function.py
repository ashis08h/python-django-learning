def func1(val1):
    val1 = val1 + 1
    print("Print the value inside func", val1)


val1 = 10
func1(val1)
print("the value from outside of function", val1)


def func2(list1):
    list1.append(8)
    print("print the list inside func2", list1)


list1 = [1, 2, 3]
func2(list1)
print("print the list outside of func2", list1)
