# 03_random 모듈
# 표준 라이브러리의 random 모듈은 '랜덤한 숫자를 생성' 위한 함수를 제공한다.
import random

# randint 함수
# randint 는 두 수 사이의 랜덤한 '정수' 를 리턴한다.
# randint(a, b) 를 하면 a <= N <= b 를 만족하는 임의의 '정수' N 을 리턴.

print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))

# uniform 함수(function)
# uniform 은 두 수 사이의 랜덤한 '소수' 를 리턴한다.
# uniform(a, b) 를 하면 a <= N <= b 를 만족하는 임의의 '소수' N 을 리턴.

print(random.uniform(0, 2))
print(random.uniform(0, 2))
print(random.uniform(0, 2))
print(random.uniform(0, 2))
print(random.uniform(0, 2))
