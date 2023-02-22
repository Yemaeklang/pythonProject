# strip : 문자열의 앞뒤에 있는 white space 를 없애는 역할 수행
# white space : 공백을 의미 " ", "\t", "\n" (space, tap, enter)
print("     abc   def      ")
print("     abc   def      ".strip())
print("       \td    \n   abc   def \n\n\n")
print("       \td    \n   abc   def \n\n\n".strip())
print("strip")
with open('data/chicken.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(line.strip())
