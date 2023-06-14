'''
<프로그래머스 직사각형 넓이 구하기>
2차원 좌표 평면에 변이 축과 평행한 직사각형이 있습니다. 
직사각형 네 꼭짓점의 좌표 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]가 담겨있는 배열 dots가 매개변수로 주어질 때, 
직사각형의 넓이를 return 하도록 solution 함수를 완성해보세요.
'''

# 내 풀이
def solution(dots):
    x = max(i[0] for i in dots) - min(i[0] for i in dots)
    y = max(i[1] for i in dots) - min(i[1] for i in dots)
    return abs(x)*abs(y)

# 다른이 풀이
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])

'''
생각보다 아이지어가 많이 벗어나지는 않는데 조금 더 깔끔하게 코드 쓰는 법을 참고하기!
'''

