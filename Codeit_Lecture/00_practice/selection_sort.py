def selection_sort(unsorted_list):
    new_list = list(unsorted_list)
    i = 0
    while i < len(new_list) - 1:
        j = i + 1
        while j < len(new_list):
            if new_list[i] > new_list[j]:
                temp = new_list[i]
                new_list[i] = new_list[j]
                new_list[j] = temp
            j += 1
        i += 1
    return new_list


# test code
my_numbers = [4, 2, 7, 1, 9, 3, 8, 5, 6]

print(selection_sort(my_numbers))
print(my_numbers)
