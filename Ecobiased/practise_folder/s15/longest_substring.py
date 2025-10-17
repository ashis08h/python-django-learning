def longest_substring(input_string):
    result = []
    count_list = []
    temp_list = []
    count = 0

    for char in input_string:
        if char not in temp_list:
            temp_list.append(char)
            count += 1
        else:
            result.append(temp_list)
            count_list.append(count)
            count = 1
            temp_list = [char]
    max_count_char = max(count_list)
    max_count_index = count_list.index(max_count_char)
    result_list = result[max_count_index]
    return ''.join(result_list)


print(longest_substring("abcdeabcdefbb"))
print(longest_substring("abc adef ghij jkl"))