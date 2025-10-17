def extedn_list(value, list=[]):
    list.append(value)
    return list


print(extedn_list(10))
print(extedn_list(123, []))
print(extedn_list('a'))
