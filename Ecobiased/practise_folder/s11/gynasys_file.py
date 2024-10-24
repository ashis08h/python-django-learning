def extend_list(value, list=[]):
    list.append(value)
    return list


print(extend_list(10))
print(extend_list(123, []))
print(extend_list('a'))