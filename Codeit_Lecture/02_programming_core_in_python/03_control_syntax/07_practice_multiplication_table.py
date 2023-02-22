# 실습 설명
# while문을 사용해서 구구단 프로그램을 만들어 봅시다.
# 실행하면 아래와 같은 결과물이 출력되어야 합니다.
#
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# .
# .
# .
# 9 * 7 = 63
# 9 * 8 = 72
# 9 * 9 = 81
N = 1
while N <= 9:
    n = 1
    while n <= 9:
        print(f"{N} * {n} = {N * n}")
        n += 1
    N += 1
