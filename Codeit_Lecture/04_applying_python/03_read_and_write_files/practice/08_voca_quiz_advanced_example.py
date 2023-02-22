# import random
#
# with open('vocabulary.txt', 'r', encoding='utf-8') as f:
#     voca = f.readlines()
#     while True:
#         line_num = random.randint(0, len(voca) - 1)
#         line = voca[line_num]
#         data = line.strip().split(": ")
#         eng = data[0]
#         kor = data[1]
#
#         answer = input(f"{kor}: ")
#         if answer == 'q':
#             break
#         elif answer == eng:
#             print("맞았습니다!\n")
#         else:
#             print(f"틀렸습니다. 정답은 {eng}입니다.\n")

import random

# 사전 만들기
voca = {}
with open('vocabulary.txt', 'r', encoding='utf-8') as f:
    for line in f:
        data = line.strip().split(": ")
        eng, kor = data[0], data[1]
        voca[eng] = kor

# 목록 가져오기
keys = list(voca.keys())

# 문제 출제
while True:
    # 랜덤한 문제 출제
    index = random.randint(0, len(keys) - 1)
    eng = keys[index]
    kor = voca[eng]

    # 사용자 입력값 받기
    guess = input(f"{kor}: ").strip()

    # 프로그램 종료
    if guess == 'q':
        break
    # 정답 확인
    elif guess == eng:
        print("맞았습니다!\n")
    else:
        print(f"틀렸습니다. 정답은 {eng}입니다.\n")
