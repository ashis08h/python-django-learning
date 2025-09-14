# example of bubble sort

def bubble_sort(input_list):
    len_of_input_list = len(input_list)
    for index in range(len_of_input_list):
        for iter in range(len_of_input_list - index - 1):
            if input_list[iter] > input_list[iter + 1]:
                input_list[iter], input_list[iter + 1] = input_list[iter + 1], input_list[iter]
    return input_list


print(bubble_sort([64, 34, 25, 12, 64, 22, 11, 90]))


def selection_sort(input_list):
    len_of_input_list = len(input_list)
    for index in range(len_of_input_list):
        min_index = index
        for iter in range(index + 1, len_of_input_list):
            if input_list[min_index] > input_list[iter]:
                min_index = iter
        input_list[min_index], input_list[index] = input_list[index], input_list[min_index]
    return input_list


print(selection_sort([64, 34, 25, 12, 64, 22, 11, 90]))


def insertion_sort(input_list):
    len_of_input_list = len(input_list)
    for index in range(1, len_of_input_list):
        key = input_list[index]
        num = index - 1

        while num >= 0 and key < input_list[num]:
            input_list[num + 1] = input_list[num]
            num -= 1
        input_list[num+1] = key
    return input_list


print(insertion_sort([64, 34, 25, 12, 64, 22, 11, 90]))


def merge_sort(input_list):

    if len(input_list) > 1:
        mid = len(input_list) // 2
        first_half = input_list[:mid]
        second_half = input_list[mid:]
        merge_sort(first_half)
        merge_sort(second_half)

        i = j = k = 0
        while i < len(first_half) and j < len(second_half):
            if first_half[i] < second_half[j]:
                input_list[k] = first_half[i]
                i += 1
            else:
                input_list[k] = second_half[j]
                j += 1
            k += 1
        while i < len(first_half):
            input_list[k] = first_half[i]
            i += 1
            k += 1
        while j < len(second_half):
            input_list[k] = second_half[j]
            j += 1
            k += 1
    return input_list


data = [64, 34, 25, 12, 64, 22, 11, 90]
print(merge_sort(data))


def quick_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        mid = len(input_list) // 2
        pivot = input_list[mid]
        left_list = [x for x in input_list if x < pivot]
        right_list = [x for x in input_list if x > pivot]
        middle = [x for x in input_list if x == pivot]
        return quick_sort(left_list) + middle + quick_sort(right_list)


data = [64, 34, 25, 12, 22, 11, 90, 64]
print(quick_sort(data))


def timsort(input_list):
    return sorted(input_list)


print(timsort([64, 34, 25, 12, 22, 64, 11, 90]))