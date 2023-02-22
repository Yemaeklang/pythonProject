# format method
# 저는 박지성, 유재석, 빌 게이츠를 좋아합니다.
print("저는 {}, {}, {}를 좋아합니다!".format("박지성", "유재석", "빌 게이츠"))
# 박지성, 유재석, 빌 게이츠 순서 바꾸기
print("저는 {2}, {0}, {1}를 좋아합니다!".format("박지성", "유재석", "빌 게이츠"))

# 2 / 3 에서의 fomat method 예시
num_1 = 1
num_2 = 3
# 일반
print("{0} 나누기 {1}은 {2}입니다.".format(num_1, num_2, num_1 / num_2))
# 소수점 2 자리
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1 / num_2))
# 소수점 4자리
print("{0} 나누기 {1}은 {2:.4f}입니다.".format(num_1, num_2, num_1 / num_2))
# 정수형
print("{0} 나누기 {1}은 {2:.1f}입니다.".format(num_1, num_2, num_1 / num_2))
print(f"{num_1} 나누기 {num_2}은 {int(num_1 / num_2)}입니다.")

# format method 유형 및 예시
name = "이재필"
age = 30
# 초기 방식(%s, %d, %f 등)
print("제 이름은 %s입니다. 나이는 만 %d입니다." % (name, age))
# print("{}{}{}".format(a,b,c)) : 2020년 2월 기준 가장 대중적인 방식
print("제 이름은 {}입니다. 나이는 만 {}입니다.".format(name, age))
# f-string : python version 3.6부터 새로나온 방식
print(f"제 이름은 {name}입니다. 나이는 만 {age}입니다.")
