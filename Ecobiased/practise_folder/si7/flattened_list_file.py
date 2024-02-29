def flattened_list(input_list):
    flattened_lists = []
    for element in input_list:
        if isinstance(element, list):
            flattened_lists.append(flattened_list(element))
        else:
            flattened_lists.append(element)
    return flattened_lists


print(flattened_list([[1, 2, 3], [4, 5, 6], [7, [8, 9], 10]]))
