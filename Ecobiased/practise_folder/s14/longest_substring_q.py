def longest_substring(input_str):
    result = []
    temp_list = []
    count_list = []
    count = 0
    for char in input_str:
        if char not in temp_list:
            temp_list.append(char)
            count += 1
        else:
            count_list.append(count)
            result.append(temp_list)
            count = 1
            temp_list = []
            temp_list.append(char)
    max_count = max(count_list)
    max_count_index = count_list.index(max_count)
    return "".join(result[max_count_index])


print(longest_substring("abcdeabcdefbb"))
print(longest_substring("abc adef ghij jkl"))
