#method - 2

input_str = "abc adef ghij jkl"
# output: "abc"

result = []
count = 0
temp_list = []
count_list = []
for item in input_str:
    if item not in temp_list:
        print("if", item)
        temp_list.append(item)
        count += 1
        print(count)
    else:
        print("else", item)
        result.append(temp_list)
        temp_list = []
        count_list.append(count)
        count = 1

        temp_list.append(item)
print(result)
print(count_list)
max_count = max(count_list)
print("".join(result[count_list.index(max_count)]))









