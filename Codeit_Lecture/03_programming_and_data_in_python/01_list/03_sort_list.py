# 리스트 정렬
numbers = [19, 13, 2, 5, 3, 11, 7, 17]  # 무작위 순서로 리스트
print(numbers)
# reverse 메소드 : 리스트의 순서를 뒤집어서 배치한다. 리턴값이 없다.
print("reverse 메소드")
numbers.reverse()
print(numbers)
# sorted 함수 : 정렬하여 리턴한다. 기존 리스트를 변경하지 않는다.
print("sorted 함수")
new_list = sorted(numbers)  # 작은 순서로 정렬
print(new_list)
new_list = sorted(numbers, reverse=True)  # 큰 순서로 정렬
print(new_list)
print(f"""sorted 함수는 기존 리스트를 변경하지 않는다.
print(numbers) : """, numbers)
# sort 메소드 : 리스트를 정렬하여 변경한다. 리턴값이 없다.
print("sort 메소드")
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
