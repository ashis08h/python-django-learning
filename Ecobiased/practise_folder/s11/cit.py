a_list = [10, 30, 20, 40, 50]

# process 1
a_list.sort()
print(a_list[-2])

# process 2
b_list = [10, 30, 20, 40, 50]
max_1 = max(b_list)
b_list.remove(max_1)
max_2 = max(b_list)
print(max_2)


def add_extra(func):
    def wrapper():
        result = func()
        return result + 10
    return wrapper


@add_extra
def add_number():
    return 2 + 3


print(add_number())


a_dict = {
    "name": "ashish",
    "nebour": "ashish",
    "lastname": "kumar"
}

result_list = []
result_dict = {}
for key, value in a_dict.items():
    if value not in result_list:
        result_dict[key] = value
        result_list.append(value)

print(result_dict)


# select item, location from table_1 groub by item, location having count(1) > 1
#
#
#
# with duplicate_item as (
# select item as item from table_1 groub by item having count(1) > 1
# ) delete from table_1 where item in (select item in duplicate_item);

