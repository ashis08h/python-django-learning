def flatened_list(input_list):
    result = []
    for element in input_list:
        if isinstance(element, list):
            result.extend(flatened_list(element))
        else:
            result.append(element)
    return result


print(flatened_list([[1, 2, 3], [4, 5, 6], [7, [8, 9], 10, 2]]))


input_list = [1, 2, 3, 4, [0, 6, 8], 9, [33, 44]]
main_list = []

list(main_list.extend(element) if isinstance(element, list) else main_list.append(element) for element in input_list)
print(main_list)