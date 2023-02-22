# 실습 설명
# 영어 강사 Coy는 학생들의 단어 암기를 위해 단어장 프로그램을 만들려고 합니다.
#
# 이 프로그램은 콘솔로 영어 단어와 한국어 뜻을 받고,
# vocabulary.txt라는 새로운 텍스트 파일에 단어와 뜻을 정리하는데요.
# 사용자가 새로운 단어와 뜻을 입력할 때마다 vocabulary.txt에 작성되는 것입니다.
#
# 사용자는 반복적으로 단어와 뜻을 입력하는데,
# 단어나 뜻으로 q를 입력하는 순간 프로그램은 즉시 종료됩니다.
# 사용자가 q를 입력하고 나면 파일은 더 이상 바뀌지 않아야 합니다.
#
# 사용자가 q를 입력하면 프로그램이 종료되고,
# vocabulary.txt에 다음과 같이 단어들이 정리되어 있어야 합니다.
#
# cat: 고양이
# apple: 사과
# church: 교회
# temple: 절
# wallet: 지갑
# backpack: 책가방
# soap: 비누
# bicycle: 자전거

with open('vocabulary.txt', 'w', encoding='utf-8') as f:
    while True:
        eng = input("영어 단어를 입력하세요: ")
        if eng == '':
            while eng == '':
                eng = input("영어 단어를 입력하세요: ")
        elif eng == 'q':
            break
        f.write(f"{eng}: ")

        kor = input("한국어 뜻을 입력하세요: ")
        if kor == '':
            while kor == '':
                kor = input("한국어 뜻을 입력하세요: ")
        elif kor == 'q':
            break
        f.write(f"{kor}\n")
