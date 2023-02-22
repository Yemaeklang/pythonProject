# 02 range 함수
# 1 부터 10 까지 출력
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)

# 1 부터 100까지 출력의 경우에는?
# range 함수 이용
#
# <형태>
# range 의 파라미터 1개 : 0 부터 stop - 1 의 범위
# for 변수 in range(stop):
#     실행문
#
# range 의 파라미터 2개 : start 부터 stop - 1 의 범위
# for 변수 in range(start, stop):
#     실행문
#
# range 의 파라미터 3개 : start 부터 stop - 1 의 범위, step 간격
# for 변수 in range(start, stop, step):
#     실행문
#
print()
# example
num = []
print(num)
for i in range(0, 100, 33):
    print(i)
    num.append(i)
    print(num)

# range 함수는 지정된 규칙에 맞춰서 값을 가져오지만
# 컴퓨터의 메모리를 지속적으로 사용하지 않는다. == 값의 저장 X
print(range(0, 100, 33))
extra_practice = range(0, 100, 33)
print(extra_practice)
