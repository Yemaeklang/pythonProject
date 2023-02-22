# format을 이용한 문자열 포맷팅

# 오늘은 2019년 10월 29일입니다.
year = 2019
month = 10
day = 29

print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일입니다.")
print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))

# 오늘은 2019년 10월 30일입니다.
date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day + 1))
