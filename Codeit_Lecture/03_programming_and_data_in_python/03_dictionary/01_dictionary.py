# 01 사전 (dictionary)
print("\n01 사전 (dictionary)\n")
# key-value pair (키-값 쌍)
my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}

print(type(my_dictionary))  # class는 dict
print(my_dictionary[3])  # 키 3의 값 출력
my_dictionary[9] = 81  # 키 9에 81을 저장
print(my_dictionary)

print()
#  list와 달리 정수가 아닌 키에 값 저장이 가능하다.
my_family = {
    "엄마": "김자옥",
    "아빠": "이석진",
    "아들": "이동민",
    "딸": "이지영"
}

print(my_family['아빠'])
