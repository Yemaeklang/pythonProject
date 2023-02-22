# 실습 설명
# 함수 sum_digit은 파라미터로 정수형 num을 받고, num의 각 자릿수를 더한 값을 리턴합니다.
#
# 예를 들어서 12의 각 자릿수는 1, 2이니까 sum_digit(12)는 3(1 + 2)을 리턴합니다.
#
# 마찬가지로 486의 각 자릿수는 4, 8, 6이니까 sum_digit(486)은 18(4 + 8 + 6)을 리턴하는 거죠.
#
# 여러분이 해야 할 일은 두 가지입니다.
#
# sum_digit 함수를 작성한다.
# sum_digit(1)부터 sum_digit(1000)까지의 합을 구해서 출력한다.
# 실습 결과
# 13501
# 자리수 합 리턴
def sum_digit(num):
    # 여기에 코드를 작성하세요
    digit_sum = 0
    str_num = str(num)

    for digit in str_num:
        digit_sum += int(digit)

    return digit_sum


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 여기에 코드를 작성하세요
result = 0
for number in range(1, 1001):
    result += sum_digit(number)

print(result)

# while 문
result = 0
number = 1
while number <= 1000:
    result += sum_digit(number)
    number += 1

print(result)
