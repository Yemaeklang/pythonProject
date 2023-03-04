def binary_search(element, some_list):
    if element not in some_list:
        return None
    else:
        temp_min = 0
        temp_max = len(some_list)
        while True:
            if element == some_list[(temp_min + temp_max) // 2]:
                return (temp_min + temp_max) // 2
            elif element > some_list[(temp_min + temp_max) // 2]:
                temp_min = (temp_min + temp_max) // 2 + 1
            else:
                temp_max = (temp_min + temp_max) // 2


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
