# scope(범위)
# scope: 변수가 사용 가능한 범위
# 로컬 변수 : 변수를 정의한 함수 내에서만 사용 가능
# 글로벌 변수 : 모든 곳에서 사용 가능
# 함수에서 변수를 사용하면, 로컬 변수를 먼저 찾고나서
# 로컬변수가 없을 시 글로벌 변수를 찾음.
def my_function():
    x = 3  # x는 로컬 변수로 함수 내에서만 정의된 것.
    print(x)


my_function()
print("""
def my_function():
    x = 3  # x는 로컬 변수로 함수 내에서만 정의된 것.
    print(x)

my_funtion() : 3
print(x) : error
# print(x) 실행 시 x는 로컬 변수이므로
# 함수 밖에서는 정의되지 않아 오류가 발생한다.
""")

###
x2 = 2  # x2는 글로벌 변수. 이후 모든 범위에서 정의됨.


def my_function_second():
    print(x2)


my_function_second()
print(x2)

###
x3 = 1  # 글로벌 변수 x3


# noinspection PyShadowingNames
def my_function_third():
    x3 = 4  # 로컬 변수 x_3
    print(x3)


my_function_third()
print(x3)
