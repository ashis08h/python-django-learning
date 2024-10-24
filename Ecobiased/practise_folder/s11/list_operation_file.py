a_list = [1, 3, 5, 6, 8, 3, 5, 8, 0]

while 8 in a_list:
    a_list.remove(8)
print(a_list)

a_list.append(8)
a_list.append(8)

print(a_list)

print(a_list.count(8))
print(a_list.index(8))

a_str = "ashish"
print(a_str.index('h'))
print(a_str.rindex('h'))