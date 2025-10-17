input_str = "abc adef ghij jkl"
# output: "abc"
result = []
count = 0
temp_list = []
count_list = []
for item in input_str:
    if item not in temp_list:
        temp_list.append(item)
        count += 1
    else:
        result.append(temp_list)
        temp_list = []
        count_list.append(count)
        count = 1

        temp_list.append(item)
max_count = max(count_list)
print("".join(result[count_list.index(max_count)]))

result = []
count_list = []
temp_list = []
count = 0

for char in input_str:
    if char not in temp_list:
        temp_list.append(char)
        count += 1
    else:
        result.append(temp_list)
        count_list.append(count)
        count = 1
        temp_list = [char]

max_count = max(count_list)
max_index = count_list.index(max_count)
result_list = result[max_index]
print("".join(result_list))








