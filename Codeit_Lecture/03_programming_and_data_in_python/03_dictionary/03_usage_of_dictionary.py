# 03 사전 활용법
print("\n\n03 사전 활용법\n")
my_family = {
    '엄마': '김자옥',
    '아빠': '이석진',
    '아들': '이동민',
    '딸': '이지영'
}

print(my_family.values())  # 사전에 어떤 값들이 있는지 목록을 출력
print()
print('이지영' in my_family.values())  # 사전에 값 '이지영' 이 존재하는지 확인
print('이재필' in my_family.values())  # 불린(boolin)값으로 확인한다.

print()
for value in my_family.values():  # 사전의 값으로 반복문 실행
    print(value)

print()
print(my_family.keys())  # 사전의 키 목록을 출력
for key in my_family.keys():  # 사전의 키로 반복문 실행
    print(key)

print()
# 사전의 키와 값을 출력
for key in my_family.keys():  # 변수 key에 키 값을 지정하는 for문
    value = my_family[key]  # 지정된 key에 해당하는 값을 변수 value에 저장
    print(key, value)  # 변수 key와 value 출력

print()
# key와 value를 동시해 받아오는 방법
for key, value in my_family.items():
    print(key, value)
