# while 반복문을 사용하여 1 이상 100 이하의 짝수를 모두 출력해 보세요.

even_number = 1
while even_number <= 100:
    if even_number % 2 == 0:  # 짝수
        print(even_number)
        even_number += 1
    else:
        even_number += 1

print()
some_number = 1
while some_number * 2 - 1 <= 100:  # 홀수
    print(some_number * 2 - 1)
    some_number += 1
