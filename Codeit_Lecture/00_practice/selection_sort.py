def sorting(list):
    i = 0
    while i < len(list) - 1:
        j = i + 1
        while j < len(list):
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
            j += 1
        i += 1
    return list

# test code
my_numbers = [4, 2, 7, 1, 9, 3, 8, 5, 6]

print(sorting(my_numbers))