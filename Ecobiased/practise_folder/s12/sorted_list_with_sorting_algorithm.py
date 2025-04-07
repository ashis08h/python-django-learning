# example of buble sort

def bubble_sort(input_list):
    len_of_input_list = len(input_list)
    for iter in range(len_of_input_list):
        for num in range(len_of_input_list - iter - 1):
            if input_list[num] > input_list[num + 1]:
                input_list[num], input_list[num + 1] = input_list[num + 1], input_list[num]
    return input_list


print(bubble_sort([64, 34, 25, 12, 64, 22, 11, 90]))


# example of selection sort

def selection_sort(input_list):
    len_of_input_list = len(input_list)
    for iter in range(len_of_input_list):
        min_index = iter
        for num in range(iter + 1, len_of_input_list):
            if input_list[min_index] > input_list[num]:
                min_index = num
        input_list[min_index], input_list[iter] = input_list[iter], input_list[min_index]
    return input_list


print(selection_sort([64, 34, 25, 12, 64, 22, 11, 90]))


# Example of insertion sort

def insertion_sort(input_list):
    len_of_input_list = len(input_list)

    for iter in range(1, len_of_input_list):
        key = input_list[iter]
        num = iter - 1
        while num >=0 and key < input_list[num]:
            input_list[num + 1] = input_list[num]
            num -= 1
        input_list[num + 1] = key
    return input_list([64, 34, 25, 12, 64, 22, 11, 90])


# example of merge sort

def merge_sort(input_list):
    if len(input_list) > 1:
        mid = len(input_list) // 2
        left_half = input_list[:mid]
        right_half = input_list[mid:]
        merge_sort(left_half) # recursive call on the left half
        merge_sort(right_half) # recursive call on the right half

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                input_list[k] = left_half[i]
                i += 1
            else:
                input_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            input_list[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            input_list[k] = right_half[j]
            j += 1
            k += 1
    return input_list


data = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(data))


# example of quick sort

def quick_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    mid = len(input_list) // 2
    pivot = input_list[mid]
    left = [x for x in input_list if x < pivot]
    right = [x for x in input_list if x > pivot]
    middle = [x for x in input_list if x == pivot]
    return quick_sort(left) + middle + quick_sort(right)


data = [64, 34, 25, 12, 22, 11, 90]
print(quick_sort(data))


# example of timsort python builtin sort

def timsort(input_list):
    return sorted(input_list)


print(timsort([64, 34, 25, 12, 22, 11, 90]))