# if문 구조
#
# if 조건 부분:  # 참과 거짓을 확인하고 싶은 조건
#     수행 부분  # 참일 때 수행할 동작
#
# 예제
from random import randrange

temperature = randrange(-20, 35)
print(f"섭씨 {temperature} 도")
if temperature <= 10:  # temperature 변수가 10보다 작거나 같은지 확인
    print("자켓을 입는다.")  # 참일 경우에 동작
else:  # 거짓일 경우
    print("자켓을 입지않는다.")  # 거짓일 경우에 동작
