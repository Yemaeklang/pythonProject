# format method 유형 및 예시
name = "이재필"
age = 30
# 초기 방식(%s, %d, %f 등)
print("제 이름은 %s입니다. 나이는 만 %d입니다." % (name, age))
# print("{}{}{}".format(a,b,c)) : 2020년 2월 기준 가장 대중적인 방식
print("제 이름은 {}입니다. 나이는 만 {}입니다.".format(name, age))
# f-string : python version 3.6부터 새로나온 방식
print(f"제 이름은 {name}입니다. 나이는 만 {age}입니다.")
