# 실습 설명
# 현명하게 거스름돈을 계산해 주는 프로그램을 만들려고 합니다. 예를 들어 33,000원짜리 물건을 사기 위해 100,000원을 냈다면,
#
# 50,000원 1장
# 10,000원 1장
# 5,000원 1장
# 1,000원 2장
# 이런 식으로 '가장 적은 수'의 지폐를 거슬러 주는 것입니다. 방금 같은 경우에는 총 5장을 거슬러 준 거죠.
#
# 우리는 calculate_change라는 함수를 작성하려고 하는데요. 이 함수는 지불한 금액을 나타내는 payment와 물건의 가격을 나타내는 cost를 파라미터로 받습니다.
#
# 아래의 코드에 이어서 깔끔하게 프로그램을 작성해 보세요.
#
# def calculate_change(payment, cost):
#     # 여기에 코드를 작성하세요
#
#
#
# # 테스트 코드
# calculate_change(100000, 33000)
# print()
# calculate_change(500000, 378000)
# 함수를 쓰고 프로그램을 실행하면 아래와 같은 결과값이 콘솔에 출력되어야 합니다.
#
# 50000원 지폐: 1장
# 10000원 지폐: 1장
# 5000원 지폐: 1장
# 1000원 지폐: 2장
#
# 50000원 지폐: 2장
# 10000원 지폐: 2장
# 5000원 지폐: 0장
# 1000원 지폐: 2장
def calculate_change(payment, cost):
    # 여기에 코드를 작성하세요
    change = payment - cost
    krw_fifty_thousand = change // 50000
    krw_ten_thousand = (change % 50000) // 10000
    krw_five_thousand = (change % 10000) // 5000
    krw_one_thousand = (change % 5000) // 1000
    print(f"""50000원 지폐: {krw_fifty_thousand}장
10000원 지폐: {krw_ten_thousand}장
5000원 지폐: {krw_five_thousand}장
1000원 지폐: {krw_one_thousand}장""")


# 테스트 코드
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
