# 실습 설명
# 피보나치 수열(Fibonacci Sequence)라고 들어 보셨나요?
#
# 1
# ,
# 1
# ,
# 2
# ,
# 3
# ,
# 5
# ,
# 8
# ,
# 13
# ,
# 21
# ,
# 34
# ,
# 55
# ,
# .
# .
# .
# 1,1,2,3,5,8,13,21,34,55,...
#
# 우선 피보나치 수열의 1번 항과 2번 항은 각각 1입니다. 3번 항부터는 바로 앞 두 항의 합으로 계산됩니다.
# 예를 들어서 3번 항은 1번 항(1)과 2번 항(1)을 더한 2이며, 4번 항은 2번 항(1)과 3번 항(2)을 더한 3입니다.
#
# 피보나치 수열의 첫 50개 항을 차례대로 출력하는 프로그램을 작성해 보세요.
#
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# .
# .
# .
# 4807526976
# 7778742049
# 12586269025
sequence = 1
fibo1 = 1
fibo = 1
while sequence <= 50:
    if sequence <= 2:
        print(1)
    else:
        fibo = fibo1 + fibo
        print(fibo)
        fibo1 = fibo - fibo1
    sequence += 1
