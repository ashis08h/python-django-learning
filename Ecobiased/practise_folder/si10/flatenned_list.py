def flattened_list(input_list):
    result_list = []
    for element in input_list:
        if isinstance(element, list):
            result_list.extend(flattened_list(element))
        else:
            result_list.append(element)
    return result_list


print(flattened_list([[1, 2, 3], [4, 5, 6], [7, [8, 9], 10, 2]]))
