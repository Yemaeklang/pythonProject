# 실습 설명
# 지난 실습 과제에서 단어장 퀴즈 프로그램을 만들었는데요.
# 학생들이 문제의 순서가 매번 똑같아서 재미가 없다고 합니다.
#
# 이번에는 random 모듈과 사전(dictionary)을 이용해서
# vocabulary.txt의 단어들을 랜덤한 순서로 내도록 프로그램을 바꿔 보세요.
#
# 같은 단어를 여러번 물어봐도 괜찮고,
# 프로그램은 사용자가 알파벳 q를 입력할 때까지 계속 실행됩니다.
#
# 프로그램 동작 예시
# 교회: church
# 맞았습니다!
#
# 사과: apple
# 맞았습니다!
#
# 자전거: bicycle
# 맞았습니다!
#
# 지갑: wallet
# 맞았습니다!
#
# 교회: church
# 맞았습니다!
#
# 절: tample
# 틀렸습니다. 정답은 temple입니다.
#
# 비누: soap
# 맞았습니다!
#
# 고양이: dog
# 틀렸습니다. 정답은 cat입니다.
#
# 자전거: q

import random

with open('vocabulary.txt', 'r', encoding='utf-8') as voca:
    voca = voca.readlines()
    while True:
        line_num = random.randint(0, len(voca) - 1)
        line = voca[line_num]
        data = line.strip().split(": ")
        eng = data[0]
        kor = data[1]
        answer = input(f"{kor}: ")
        if answer == 'q':
            break
        elif answer == eng:
            print("맞았습니다!\n")
        else:
            print(f"틀렸습니다. 정답은 {eng}입니다.\n")
