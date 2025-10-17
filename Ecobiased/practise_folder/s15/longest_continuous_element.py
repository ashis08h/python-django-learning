ips= [1, 2, 3, 3, 4, 5, 6, 1, 2, 1, 2, 3, 4, 5, 6]

longest = []
temp_list = []
count_list = []
count = 0

for index in range(len(ips)):
    if index == 0:
        temp_list.append(ips[index])
        count += 1
    elif ips[index] - ips[index - 1] == 1:
        temp_list.append(ips[index])
        count += 1
        if index == len(ips) -1:
            longest.append(temp_list)
            count_list.append(count)
    else:
        longest.append(temp_list)
        temp_list = [ips[index]]
        count_list.append(count)
        count = 1

max_count = max(count_list)
max_count_index = count_list.index(max_count)
result = longest[max_count_index]
print(result)

