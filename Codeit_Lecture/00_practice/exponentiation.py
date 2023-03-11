def exponentiation(base, power):
    i = 0
    res = 1
    while True:
        if i == power:
            break
        if power > 0:
            i += 1
            res *= base
        if power < 0:
            i -= 1
            res /= base
    return res


# test code
n1, n2 = map(int, input("구하고자하는 X의 n제곱에 해당하는 X, n 입력 : ").split())
print(exponentiation(n1, n2))
