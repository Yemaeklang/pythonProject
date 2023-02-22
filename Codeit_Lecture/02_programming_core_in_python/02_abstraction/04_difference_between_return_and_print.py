# return과 print의 차이
def print_square(num):
    print(num * num)


def get_square(num):
    return num * num


print_square(3)  # 3 * 3 의 결과인 9를 출력 return값은 없다.
get_square(3)  # return값이 9로 저장, 출력 X
print(get_square(3))  # 저장된 return값 9를 출력
print(print_square(3))  # print함수는 return값이 없는 경우 None을 출력

# 출력되는 None은 return값이 없다는 의미
