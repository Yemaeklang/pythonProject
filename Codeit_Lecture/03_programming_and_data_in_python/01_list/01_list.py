# 리스트(list)
# 하나의 변수에 값을 여러 개 저장하는 방법
numbers = [2, 3, 5, 7, 11, 13]
names = ["윤수", "혜린", "태호", "영훈"]
print(numbers)
print(names)
# 인덱싱 (indexing)
# 리스트에서 요소의 위치 : 인덱스(index)
# 인덱스를 통해 요소를 받아오는 것을 '인덱싱'이라 한다.
print(names[1])  # 인덱스는 0부터 시작한다.
print(numbers[1] + numbers[3])
print(numbers[-1])  # 리스트의 마지막 자리 요소
print(numbers[-4])  # 리스트의 끝에서 4번째 요소
print(numbers[-6])  # 리스트의 끝에서 6번째 요소
# 리스트 슬라이싱 (list slicing)
print(numbers[1:5])  # 리스트의 2번째 ~ 5번째 요소
print(numbers[-2:-6])  # 역순이므로 출력되는 요소가 없다.
print(numbers[-6:-2])  # 끝에서 6번째부터 2번째 이전까지 출력
print(numbers[2:])  # 3번째 요소부터 출력
print(numbers[:5])  # 6번째 요소 이전까지 출력
# 리스트 재지정
print(numbers)
numbers[0] = 8
print(numbers)
numbers[0] = numbers[2] + numbers[5]
print(numbers)
