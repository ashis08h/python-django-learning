def flatten_list(input_list):
    flattened_list = []
    for element in input_list:
        if isinstance(element, list):
            # recursion concept.
            flattened_list.extend(flatten_list(element))
        else:
            flattened_list.append(element)
    return flattened_list


#flatten_list([[1, 2, 3], [4, 5, 6], [7, [8, 9], 10]])

print(flatten_list([[1, 2, 3], [4, 5, 6], [7, [8, 9], 10]]))
