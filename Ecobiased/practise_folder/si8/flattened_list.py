def flattened_list(input_list):
    final_list = []
    for element in input_list:
        if isinstance(element, list):
            final_list.extend(flattened_list(element))
        else:
            final_list.append(element)
    return final_list


print(flattened_list([[1, 2, 3], [4, 5, 6], [7, [8, 9], 10]]))
