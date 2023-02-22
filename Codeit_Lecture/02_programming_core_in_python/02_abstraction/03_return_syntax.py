# return문 제대로 이해하기
def square2(num):
    print("함수 시작")
    return num * num  # return문 : 함수에 값을 돌려주고 함수 종료
    print("함수 끝")  # dead code : 무의미한 코드(함수가 종료되어 실행 X)


print("print(square2(3)) : ", square2(3))
print("Hello World!")
