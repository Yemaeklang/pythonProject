# 리스트에서 값의 존재 확인하기
def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        if some_list[i] == value:
            return True
        i += 1

    return False


# 값의 존재 확인 테스트
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7))
print(in_list(primes, 12))
# 리스트에 값의 존재를 확인하는 것은 너무 자주 있는 일이라서
# 파이썬에 이미 이 기능이 내장되어 있다.
# in이라는 키워드를 쓰면 됩니다.
print(7 in primes)
print(12 in primes)
# 거꾸로 값이 없는지 확인하려면 in 앞에 not을 붙인다.
print(7 not in primes)
print(12 not in primes)
print()

# 리스트 안의 리스트 (Nested list)
# 세 번의 시험을 보는 수업
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]
# 첫 번째 학생의 성적
print(grades[0])
# 세 번째 학생의 성적
print(grades[2])
# 첫 번째 학생의 첫 번째 시험 성적
print(grades[0][0])
# 세 번째 학생의 두 번째 시험 성적
print(grades[2][1])
# 첫 번째 시험의 평균
print((grades[0][0] + grades[1][0] + grades[2][0]) / 3)
