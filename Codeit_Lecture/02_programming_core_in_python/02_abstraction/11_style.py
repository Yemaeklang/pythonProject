# 스타일
# python 스타일 가이드 : PEP8
print("""
python의 코딩 스타일 가이드인 PEP8을 따르도록 하자.
""")
print("""
### Before
print(6.28*4)
print(3.14*4*4)
print(6.28*8)
print(3.14*8*8)
""")
print(6.28 * 4)
print(3.14 * 4 * 4)
print(6.28 * 8)
print(3.14 * 8 * 8)

print("""
### After
PI = 3.14


def circle_area(r):
    return r * r * PI


def circle_length(r):
    return 2 * r * PI

radius = 4
print(circle_length(radius))
print(circle_area(radius))

radius = 8
print(circle_length(radius))
print(circle_area(radius))
""")

PI = 3.14


def circle_area(r):
    return r * r * PI


def circle_length(r):
    return 2 * r * PI


radius = 4
print(circle_length(radius))
print(circle_area(radius))

radius = 8
print(circle_length(radius))
print(circle_area(radius))
