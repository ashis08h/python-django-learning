def longest_unique_string(input_string):
    seen = {}
    start = 0
    longest = ""

    for end, char in enumerate(input_string):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = end

        if end - start + 1 > len(longest):
            longest = input_string[start:end + 1]
    return longest


print(longest_unique_string("abc adef ghij jkl"))

#method - 2

input_str = "abcdeabcbb"
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

