# 불러오는 모듈명을 매번 입력하지 않는 방법

from calculator import add, multiply
# calculator에서 add와 multiply 함수를 불러온다.

# from calculator import *
# 으로 calculator의 모든 함수를 불러올 수 있지만,
# 사용하는 함수의 출처가 불분명해지므로 권장하지 않는다.

print(add(2, 5))  # 정상 작동
print(multiply(3, 4))  # 정상 작동
# print(subtract(9, 2))  # 불러오지 않았으므로 오류 발생
