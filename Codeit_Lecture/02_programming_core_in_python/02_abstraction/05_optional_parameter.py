# 옵셔널 파라미터 (Optional parameter) :
# 파라미터에 기본값(default value)을 설정하여
# 파라미터의 값을 선택적으로 입력할 수 있게 하는 방법
def myself(my_name, age, nationality="한국"):  # nationality의 기본값을 "한국"으로 설정
    print("내 이름은 {}".format(my_name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))


myself("코드잇", 1, "미국")  # 옵셔널 파라미터를 제공하는 경우 : 입력값 사용
print()
myself("코드잇", 1)  # 옵셔널 파라미터를 제공하지 않는 경우 : 기본값 사용
print()


# 함수 정의에서 기본값을 설정한 매개변수는 기본값이 없는 매개변수 앞에 쓸 수 없다.
def practice_myself(my_name="이재필", age=30, nationality="한국"):
    print(f"""
내 이름은 {my_name}
국적은 {nationality}
나이는 {age}
""")


practice_myself(nationality="대한민국", age=31)
print()
