'''
<프로그래머스 평행>
점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.

[[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.

'''

# 내 풀이
def solution(dots):
    case1 = (dots[0][0] - dots[1][0]) / (dots[0][1] - dots[1][1])
    case2 = (dots[2][0] - dots[3][0]) / (dots[2][1] - dots[3][1])
    case3 = (dots[0][0] - dots[3][0]) / (dots[0][1] - dots[3][1])
    case4 = (dots[1][0] - dots[2][0]) / (dots[1][1] - dots[2][1])
    if case1 == case2 or case3 == case4:
        return 1
    else: 
        return 0
    
# 다른이 풀이1
def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]=dots
    answer1 = ((y1-y2)*(x3-x4) == (y3-y4)*(x1-x2))
    answer2 = ((y1-y3)*(x2-x4) == (y2-y4)*(x1-x3))
    answer3 = ((y1-y4)*(x2-x3) == (y2-y3)*(x1-x4))
    return 1 if answer1 or answer2 or answer3 else 0

'''
이걸 보니까 내 답이 왜 풀렸는지는 잘 모르겠지만ㅎㅎ
내 케이스에 하나를 더 추가해야 맞는 것 같다!
아무튼 이 풀이가 더 깔끔한듯!
그리고 이런식으로 리스트 내의 숫자를 변수에 한번에 저장하는게 포인트!
'''