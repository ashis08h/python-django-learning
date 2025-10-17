# example of bubble sort

def bubble_sort(input_list):

    len_of_input_list = len(input_list)
    for index in range(len_of_input_list):
        for num in range(len_of_input_list - index - 1):
            if input_list[num] > input_list[num + 1]:
                input_list[num], input_list[num + 1] = input_list[num + 1], input_list[num]
    return input_list


print(bubble_sort([64, 34, 25, 12, 64, 22, 11, 90]))


def selection_sort(input_list):

    len_of_input_list = len(input_list)

    for index in range(len_of_input_list):
        min_index = index
        for num in range(index + 1, len_of_input_list):
            if input_list[min_index] > input_list[num]:
                min_index = num
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
        left_half = input_list[:mid]
        right_half = input_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):

            if left_half[i] < right_half[j]:
                input_list[k] = left_half[i]
                i = i + 1
            else:
                input_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):

            input_list[k] = left_half[i]
            i = i +1
            k = k + 1

        while j < len(right_half):

            input_list[k] = right_half[j]
            j = j + 1
            k = k + 1
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
        middle_element = [x for x in input_list if x == pivot]
        return quick_sort(left_list) + middle_element + quick_sort(right_list)


data = [64, 34, 25, 12, 22, 11, 90, 64]
print(quick_sort(data))


def timsort(input_list):
    return sorted(input_list)


print(timsort([64, 34, 25, 12, 22, 64, 11, 90]))