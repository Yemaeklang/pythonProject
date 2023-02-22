# 100 이하의 자연수 중 8의 배수이지만 12의 배수는 아닌 것을 모두 출력
x_number = 1
while x_number <= 100:
    if x_number % 8 == 0 and x_number % 12 != 0:
        print(x_number)
    x_number += 1

print()  # 1,000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력
x_num = 1
add_num = 0
while x_num < 1000:
    if x_num % 2 == 0 or x_num % 3 == 0:
        add_num += x_num
    x_num += 1

print(add_num)

print()  # 정수 120의 약수를 모두 출력하고, 총 몇개의 약수가 있는지 출력
Num_X = 120
num_x = 1  # 약수
count = 0  # 약수의 개수
while num_x <= Num_X:
    if Num_X % num_x == 0:
        print(num_x)
        count += 1
    num_x += 1

print(f"{Num_X}의 약수는 총 {count}개입니다.")
