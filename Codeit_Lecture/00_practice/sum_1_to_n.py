# noinspection PyShadowingNames
def sum_1_to_n(n):
    # res = 0
    # i = 1
    # while i <= n:
    #     res += i
    #     if i == n:
    #         break
    #     i += 1

    #           res = 1 + 2 + 3 + ... + (n-2) + (n-1) + n
    # =>        res = n + (n-1) + (n-2) + ... + 3 + 2 + 1
    # =>  res + res = (n+1) + (n+1) + (n+1) + ... + (n+1) + (n+1) + (n+1)
    # =>      2*res = n*(n+1)  => res = (n*(n+1))/2
    res = int(n * (n + 1) / 2)

    return res


# test code
n = int(input("1부터 몇까지 더하겠습니까? : "))
print(sum_1_to_n(n))
