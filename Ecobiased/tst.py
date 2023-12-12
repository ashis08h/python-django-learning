def text_lower(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.lower()
    return wrapper

@text_lower
def hello_text(name):
    return f"My name is {name}"


print(hello_text("Ashish"))


dict1 = {1: 'name'}
print(dict1)

nam_n = "aekjskjbkjppdjfkjekppppkdkejkppsjdfshdfppdsfshdfpppp"
nam_p = "ppapp"
substring_to_search = "pp"
count = 0
occurrences_count = nam_n.count(substring_to_search)
print("occurrences_count", occurrences_count)

for index in range(len(nam_p) - 2):
    if index == 0 and nam_p[index] == 'p' and nam_p[index + 1] == 'p' and nam_p[index + 2] != 'p':
        print('test1')
        count = count + 1
    elif index != 0 and nam_p[index] == 'p' and nam_p[index + 1] == 'p' and nam_p[index +2] != 'p' and nam_p[index - 1] != 'p':
        print('test2')
        count = count + 1
print("count", count)


given=[[4,5],[[6],[7],[[[8]]]]]
output=[4,5,6,7,8]


def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

output = flatten_list(given)

print(output)



class DoubleTon:

    __count = 0
    __instance = None

    def __new__(cls):
        if cls.__count <= 1:
            cls.__instance = super().__new__(cls)
            cls.__count += 1
            return cls.__instance
        else:
            return None


s1 = DoubleTon()
s2 = DoubleTon()
s3 = DoubleTon()

print(s1)
print(s2)
print(s3)

given1=[[4,5],[[6],[7],[[[8]]]]]


def fl1(given_list):
    fl_list = []
    for item in given_list:
        if isinstance(item, list):
            fl_list.extend(fl1(item))
        else:
            fl_list.append(item)
    return fl_list


print(fl1(given1))

import re

nam_n = "aekjskjbkjppdjfkjekppppkdkejkppsjdfshdfppdsfshdfpppp"
nam_p = "ppapp"

def give_pp_count(nam_n):
    pattern = re.compile(r'(?<!p)(pp)(?!p)')
    matches = pattern.findall(nam_n)
    return len(matches)


print(give_pp_count(nam_p))

# pattern  = re.compile(r'(?<!p)(pp)(?!p)')
# match = pattern.findall(c)
# print(len(match))


