# 실습 설명
# "토마토"나 "기러기"처럼 거꾸로 읽어도 똑같은 단어를 '팰린드롬(palindrome)'이라고 부릅니다.
#
# 팰린드롬 여부를 확인하는 함수 is_palindrome을 작성하려고 하는데요.
# is_palindrome은 파라미터 word가 팰린드롬이면 True를 리턴하고 팰린드롬이 아니면 False를 리턴합니다.
#
# 예를 들어서 "racecar"과 "토마토"는 거꾸로 읽어도 똑같기 때문에 True가 출력되어야 합니다.
# 그리고 "hello"는 거꾸로 읽으면 "olleh"가 되기 때문에 False가 나와야 하는 거죠.
#
# 실습 결과
# True
# False
# True
# True
# False

def is_palindrome(word):
    reversed_word = ""
    for i in range(len(word)):
        reversed_word += word[len(word) - 1 - i]

    if reversed_word == word:
        return True
    else:
        return False


# 테스트 코드
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))

print("\n\n모범 답안\n")


# 모범 답안
def is_palindrome(word):
    for left in range(len(word) // 2):
        right = len(word) - 1 - left
        if word[left] != word[right]:
            return False

    return True


# 테스트 코드
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
