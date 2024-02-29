def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print('list1', list1)
print('list2', list2)
print('list3', list3)

# since list=[] is a mutable list by default because of that it is shared with all the instance.
