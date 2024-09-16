# example of set

a_set = {1, 2, 3, 4, 5}

print("a_set", a_set)
print("type", type(a_set))

a_set.add(6)
print(a_set)

a_set.remove(4)
print(a_set)


# example of frozenset

a_frznset = frozenset({1, 2, 3, 4, 5})
print("a_frznset", a_frznset)
print(type(a_frznset))