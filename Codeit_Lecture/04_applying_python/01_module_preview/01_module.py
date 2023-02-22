# 01_모듈 : 다른 파이썬 파일에서 사용할 수 있는 파이썬 코드를 모듈이라한다.
# 코드를 여러파일로 분리하여 사용하는 방법
import calculator  # 같은 폴더에 있는 파이썬 파일만 불러올 수 있다.

print(calculator.add(2, 5))
print(calculator.multiply(3, 4))
