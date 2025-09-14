def flatened_list(input_list):
    result_list = []
    for item in input_list:
        if isinstance(item, list):
            result_list.extend(flatened_list(item))
        else:
            result_list.append(item)
    return result_list


print(flatened_list([[1, 2, 3], [4, 5, 6], [7, [8, 9], 10, 2]]))

input_list1 = [1, 2, 3, 4, [0, 6, 8], 9, [33, 44]]

main_result_list = []

result_list = [main_result_list.extend(item) if isinstance(item, list) else main_result_list.append(item) for item in input_list1]
print(main_result_list)
