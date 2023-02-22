# 함수의 실행 순서
def hello():  # 함수 정의
    print("Hello!")
    print("Welcome to Codeit!")


print("함수 호출 전")
hello()  # hello 함수 호출
print("함수 호출 후")


def square(num):  # 함수 정의
    return num * num


print("함수 호출 전")
print("print(square(3) + square(4.0)) : ", square(3) + square(4.0))
print("함수 호출 후")
