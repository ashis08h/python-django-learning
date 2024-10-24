def flatened_list(input_list):
    result_list = []
    for item in input_list:
        if isinstance(item, list):
            result_list.extend(flatened_list(item))
        else:
            result_list.append(item)
    return result_list


print(flatened_list([[1, 2, 3], [4, 5, 6], [7, [8, 9], 10, 2]]))