# 02_standard library (표준 라이브러리) :
# 자주 쓸 법한 기능들을 모아둔 기본제공 모듈들

# 예시
import math
import os  # os는 operating system 의 약자
import random

print(math.log10(100))
print(math.cos(0))
print(math.pi)

# random모듈의 결과물은 실행할 때마다 랜덤으로 리턴
print(random.random())

# os 모듈은 파이썬으로 우리의 운영 체제를 조작하기 위한 모듈.
print(os.getlogin())  # 현재 컴퓨터에 어떤 계정으로 로그인했는지를 리턴
print(os.getcwd())  # 현재 이 파일이 있는 폴더의 경로를 리턴
