# return : 함수를 거쳐 돌려 받는 값
# print 함수는 단순 '출력', return 함수는 값을 '반환'
def get_square(x):
    return x * x


print(get_square(3))  # return으로 반환된 함수의 값을 print로 출력

y = get_square(3)
print(y)

print(get_square(3) + get_square(4))
