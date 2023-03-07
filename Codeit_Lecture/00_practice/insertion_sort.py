def insertion_sort(list_p):
    new = list(list_p)
    i = 1
    while i < len(new):
        temp = new[i]
        j = i-1
        while j >= 0:
            comp = new[j]
            if temp < comp:
                new[j+1] = comp
                new[j] = temp
            elif temp > comp:
                break
            j -= 1
        i += 1
    return new


# test code
my_list = [2, 4, 7, 1, 9, 3]
print(insertion_sort(my_list))
print(my_list)
