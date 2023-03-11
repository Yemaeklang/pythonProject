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
print(exponentiation(2, 31))
