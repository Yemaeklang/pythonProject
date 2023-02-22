from random import randint


# 이 함수는 파라미터로 정수 n을 받습니다.
# 무작위로 1과 45 사이의 서로 다른 번호 n개를 뽑고, 그 번호들이 담긴 리스트를 리턴합니다.
def generate_numbers(n):
    num_list = []  # 빈 리스트 생성

    while len(num_list) < n:
        num = randint(1, 45)
        if num not in num_list:
            num_list.append(num)

    return num_list


# 일반 당첨 번호 6개와 보너스 번호 1개가 포함된 리스트를 리턴합니다.
# 일반 당첨 번호 6개는 정렬되어 있어야 하고, 보너스 번호는 마지막에 추가하면 됩니다.
def draw_winning_numbers():
    numbers = generate_numbers(7)

    return sorted(numbers[:6]) + numbers[6:]


#  몇 개의 숫자가 일치하는지 알려 주는 함수입니다.
def count_matching_numbers(numbers, winning_numbers):
    count = 0

    for num in numbers:
        if num in winning_numbers:
            count += 1

    return count


def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus = count_matching_numbers(numbers, winning_numbers[6:])
    if count == 6:
        return 1000000000
    elif count == 5:
        if bonus == 1:
            return 50000000
        else:
            return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0
