def logarithm(base, num):
    if num <= 0 or base <= 1 or base > num:
        print("잘못된 입력. 다른 방법을 사용하세요.")
        return
    temp = num
    i = 0
    while True:
        if temp <= 1:
            break
        temp /= base
        i += 1
    return i


# Test code
b, n = map(int, input("log의 base와 number를 입력 : ").split())
print(logarithm(b, n))
