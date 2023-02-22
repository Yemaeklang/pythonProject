# 형 변환('Type Conversion' or 'Type Casting')
# 값을 한 자료형에서 '다른 자료형으로' 바꾸는 것
# ex) 정수(3) -> 소수(3.0) or 문자열("3") -> 정수(3)
print(int(3.8))  # 3
print(float(3))  # 3.0
print(int("2") + int("5"))  # 2 + 5 = 7
print(float("1.1") + float("2.5"))  # 1.1 + 2.5 = 3.6
print(str(2) + str(5))  # "2" + "5" = "25"

# print함수에서 문자열과 숫자형을 연결시킬 수 없다.
# 따라서 정수형을 문자열로 변환시켜 출력한다.
age = 7
print("제 나이는 " + str(age) + "살입니다.")
