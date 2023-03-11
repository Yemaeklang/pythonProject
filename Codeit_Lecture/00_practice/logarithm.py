def logarithm(base, num):
    if num == 0 or base <= 1 or base > num:
        print("잘못된 입력. 다른 방법을 사용하세요.")
        return
    elif num < 0:
        temp = -num
    else:
        temp = num

    i = 0
    res = 1
    while True:
        if temp <= 1:
            break
        temp /= base
        i += 1
    return i


# Test code
print(logarithm(2, 16))
