# 연산자
"""
    여러 줄 주석은 이렇게 큰 따옴표 3개를 이용합니다.
"""
width = 3
height = 5
ReactArea = width * height
TriangleArea = width*height/2

print(ReactArea)
print(width, '*', height, '=', ReactArea)

#중괄호{}를 이용해서 format method를 이용해 출력
print('{0} : {1} * {2} / 2 = {3}'.format('Triangle Area', width, height, TriangleArea))