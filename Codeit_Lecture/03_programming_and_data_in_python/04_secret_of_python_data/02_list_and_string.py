# 03_list와 string(리스트와 문자열)
# 유사점
# 리스트 인덱싱
alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

print(alphabet_list[0])
print(alphabet_list[1])
print(alphabet_list[4])
print(alphabet_list[-1])

print()
# 문자열 인덱싱
alphabet_string = 'ABCDEFGHIJ'

print(alphabet_string[0])
print(alphabet_string[1])
print(alphabet_string[4])
print(alphabet_string[-1])

print()
# 리스트 슬라이싱
print(alphabet_list[0:5])
print(alphabet_list[4:])
print(alphabet_list[:4])

print()
# 문자열 슬라이싱
print(alphabet_string[0:5])
print(alphabet_string[4:])
print(alphabet_string[:4])

print()
# 문자열 연결
str_1 = 'Hello'
str_2 = 'World'
str_3 = str_1 + str_2
print(str_3)

print()
# 리스트 연결
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = list_1 + list_2
print(list_3)

print()
# len 함수(길이 확인)
my_list = [2, 3, 5, 7, 11]
print(len(my_list))

my_string = 'Hello world!'
print(len(my_string))

print()
# 차이점
# 리스트는 인덱스 요소의 수정이 가능하다.
numbers = [1, 2, 3, 4]
numbers[0] = 5
print(numbers)

# 문자열은 인덱스 요소의 수정이 불가능하다.
print()
name = 'codeit'
# name[0] = 'C'  # 수정이 불가능하기에 오류가 발생한다.
print(name)
