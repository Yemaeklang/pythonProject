with open('vocabulary.txt', 'r', encoding='utf-8') as voca:
    for line in voca:
        quiz_data = line.strip().split(":")
        eng = quiz_data[0]
        kor = quiz_data[1]
        answer = input(f"{kor}: ")
        if answer == eng:
            print("맞았습니다!\n")
        else:
            print(f"아쉽습니다. 정답은 {eng}입니다.\n")
