# 리스트 함수
numbers = []
print(len(numbers))  # len을 통해 리스트의 길이를 리턴
numbers.append(5)  # .append를 통해 리스트 마지막에 요소 추가
print(numbers)
numbers.append(8)
print(numbers)
print()
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
print(numbers)
del numbers[3]  # del을 통해 4번째 요소 제거
print(numbers)
print("변수 numbers 의 길이 : ", len(numbers))
numbers.insert(4, 37)  # insert를 통해 5번째 자리에 37 삽입
print(numbers)
print("변수 numbers 의 길이 : ", len(numbers))
print()
# index 메소드 : 리스트에서 특정 값의 인덱스를 리턴한다.
members = ["영훈", "윤수", "태호", "혜린"]
print(members)
print("print(members.index(\"윤수\")) : ", members.index("윤수"))
print("print(members.index(\"태호\")) : ", members.index("태호"))
# remove 메소드 : 리스트에서 특정 값을 갖는 첫번째 인덱스를 삭제한다.
fruits = ["딸기", "당근", "파인애플", "수박", "참외", "파인애플", "메론"]
print(fruits)
fruits.remove("파인애플")
print(fruits)
