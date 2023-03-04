def binary_search(element, some_list):
    index_min = 0
    index_max = len(some_list) - 1
    while index_min <= index_max:
        mid_index = (index_min + index_max) // 2
        if element == some_list[mid_index]:
            return mid_index
        elif element > some_list[mid_index]:
            index_min = mid_index + 1
        else:
            index_max = mid_index - 1
    return None


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
