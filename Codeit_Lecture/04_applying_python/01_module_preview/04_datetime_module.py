# standard library 의 datetime 모듈은
# '날짜' 와 '시간' 을 다루기 위한 다양한 '클래스' 를 갖추고 있다.
import datetime

# datetime 값 생성
# 2020년 3월 14일을 파이썬으로 표현
pi_day = datetime.datetime(2020, 3, 14)
# 시각의 기본값 00:00:00

print(pi_day)
print(type(pi_day))

pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
# 13:06:15 (13시 6분 15초) 로 시각 설정

print(pi_day)
print(type(pi_day))

# 오늘 날짜
# 우리가 날짜와 시간을 정해 주는 게 아니라,
# 코드를 실행한 '지금 이 순간' 의 날짜와 시간을 받아 오고 싶다면?
today = datetime.datetime.now()

print(today)
print(type(today))

# timedelta
# 두 datetime 값 사이의 기간을 알고 싶으면, 마치 숫자 뺄셈을 하듯이 그냥 뺀다.
today = datetime.datetime.now()
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)

print(today - pi_day)
print(type(today - pi_day))
# 두 datetime 값을 빼면, timedelta 타입이 나온다.
# 날짜 간의 차이를 나타내는 타입이다.
#
# 반대로 timedelta 를 생성해서 datetime 값에 더해 줄 수도 있다.
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=5)
# my_timedelta = datetime.timedelta(5, 3, 10, 5)

print(today)
print(today + my_timedelta)

# datetime 해부하기
# datetime 값에서 '연도' 나 '월' 같은 값들을 추출하려면?
today = datetime.datetime.now()

print(today)  # 연-월-일-시-분-초-마이크로초
print(today.year)  # 연도
print(today.month)  # 월
print(today.day)  # 일
print(today.hour)  # 시
print(today.minute)  # 분
print(today.second)  # 초
print(today.microsecond)  # 마이크로초

# datetime 포맷팅
# datetime 값을 출력하면 yyyy-mm-dd hh:mm:ss.msmsms 형태.
# strftime을 사용하면, 형태를 새로 구성할 수 있다.
today = datetime.datetime.now()

print(today.strftime("%A, %B %dth %Y"))  # %A, %B, %dth, %Y 는 포맷 코드이다.
# 포맷 코드     설명                                                  예시
# %a        요일 (짧은 버전)	                                        Mon
# %A        요일 (풀 버전)	                                        Monday
# %w    	요일 (숫자 버전, 0~6, 0이 일요일)	                        5
# %d	    일 (01~31)	                                            23
# %b	    월 (짧은 버전)	                                        Nov
# %B	    월 (풀 버전)	                                            November
# %m	    월 (숫자 버전, 01~12)	                                    10
# %y	    연도 (짧은 버전)	                                        16
# %Y	    연도 (풀 버전)	                                        2016
# %H	    시간 (00~23)                  	                        14
# %I	    시간 (00~12)	                                            10
# %p	    AM/PM	                                                AM
# %M	    분 (00~59)	                                            34
# %S    	초 (00~59)	                                            12
# %f    	마이크로초 (000000~999999)                               	413215
# %Z	    표준시간대	                                            PST
# %j	    1년 중 며칠째인지 (001~366)	                            162
# %U	    1년 중 몇 주째인지 (00~53, 일요일이 한 주의 시작이라고 가정)	35
# %W	    1년 중 몇 주째인지 (00~53, 월요일이 한 주의 시작이라고 가정)	35
