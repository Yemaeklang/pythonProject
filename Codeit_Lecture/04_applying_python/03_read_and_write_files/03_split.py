# split : 파라미터를 기준으로 문자열을 나누는 함수
my_string = "1. 2. 3. 4. 5. 6"
print(my_string)
print(type(my_string))
print(my_string.split("."))
print(type(my_string.split(".")))


def my_new_string():
    new = my_string.split(".")
    for i in range(len(new)):
        new[i] = new[i].strip()
    return new


print(my_new_string())
print(my_string.split(". "))

full_name = "Kim, Yuna"
name_data = full_name.split(", ")
last_name = name_data[0]
first_name = name_data[1]

print(first_name, last_name)

# 파라미터 없이 split 사용시 화이트 스페이스를 기준으로 한다.
numbers = "   \n\n    2   \t    3   \n  5 7 11  \n\n".split()
print(numbers)
print(numbers[0], type(numbers[0]))
print(numbers[0] + numbers[1])
print(int(numbers[0]) + int(numbers[1]))
