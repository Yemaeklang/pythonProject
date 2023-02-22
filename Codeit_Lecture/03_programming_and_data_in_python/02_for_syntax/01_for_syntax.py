# for 반복문에는 조건문이 존재하지 않는다.
#
# <형태>
# for 변수 in 리스트:
#     실행문
#
# 리스트의 첫 요소부터 끝까지 for 반복문의 변수에 지정되며 진행한다.
#
# example
my_list = [2, 3, 5, 7, 11]

for number in my_list:  # number : 변수
    print(number)

print()
# 동일한 동작을 하는 while 반복문
my_list = [2, 3, 5, 7, 11]

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
