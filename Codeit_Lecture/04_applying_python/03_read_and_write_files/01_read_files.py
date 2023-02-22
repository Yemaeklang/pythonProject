# 읽어온 파일을 변수 f에 저장
# 파일을 읽을 때는 'r' : r 은 read 의 약자
# 파일을 쓸 때는 'w' : w 는 write 의 약자
# 같은 폴더에 있는 파일을 읽을 때는 '파일명'으로 읽을 수 있다.
# 다른 경로에 있을 때에는 현재 피일 위치를 기준하여 '경로/파일명'으로 불러온다.

with open('data/chicken.txt', 'r', encoding='UTF-8') as f:
    print(type(f))

    for line in f:  # 파일의 첫 줄부터 line 에 읽는다.
        print(line)
