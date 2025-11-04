input_list = [1, 3, 2, 7, 3, 5, 2, 3, 4, 3, 4, 7]
output_list = [3, 3, 3, 3, 7, 7, 4, 4, 3, 3, 5, 1]

temp_dict = {}
unique_list = []

for item in input_list:

    if item not in unique_list:
        unique_list.append(item)
        temp_dict[item] = [item]
    else:
        temp_dict[item].append(item)

sorted_dict = dict(sorted(temp_dict.items(), key=lambda x:x[0], reverse=True))
sorted_list = list(sorted_dict.values())
print(sorted(sorted_list, key=len, reverse=True))
