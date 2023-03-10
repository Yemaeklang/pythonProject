# 실습 설명
# 밑에 나와 있는 chicken.txt 파일을 보세요.
# 제가 운영하는 치킨집 '코딩에빠진닭(이하 코빠닭)'의 12월 매출이 정리되어 있습니다.
#
# 1일: 453400
# 2일: 388600
# 3일: 485300
# 4일: 477900
# 5일: 432100
# 6일: 665300
# 7일: 592500
# 8일: 465200
# 9일: 413200
# 10일: 523000
# 11일: 488600
# 12일: 431500
# 13일: 682300
# 14일: 633700
# 15일: 482300
# 16일: 391400
# 17일: 512500
# 18일: 488900
# 19일: 434500
# 20일: 645200
# 21일: 599200
# 22일: 472400
# 23일: 469100
# 24일: 381400
# 25일: 425800
# 26일: 512900
# 27일: 723000
# 28일: 613600
# 29일: 416700
# 30일: 385600
# 31일: 472300
# :의 왼쪽에는 해달 월의 며칠인지, 그리고 오른쪽에는 그 날의 매출이 적혀 있습니다.
#
# data 폴더의 chicken.txt 파일을 읽어 들이고,
# strip과 split을 써서 12월 코빠닭의 하루 평균 매출을 출력하세요.
# 평균을 구하기 위해서는 총 매출을 총 일수로 나누면 됩니다.
#
# 참고로 현재 제공된 파일에는 31일이 있지만, 어떤 달은 31일이 아닐 수도 있습니다.
# 이 점을 고려해서 확장성 있는 코드를 작성해 주시길 바랍니다.
#
# 출력 결과는 아래와 같습니다.
#
# 501916.12903225806

def average_daily_sales(file):
    days = 0
    total_sales = 0
    for line in file:
        data = line.split(':')
        daily_sales = int(data[1].strip())
        total_sales += daily_sales
        days += 1

    return total_sales / days


with open('C:/Users/USER/PycharmProjects/pythonProject/Codeit_Lecture'
          '/04_applying_python/03_read_and_write_files/data'
          '/chicken.txt', 'r', encoding='utf-8') as f:
    print(average_daily_sales(f))
