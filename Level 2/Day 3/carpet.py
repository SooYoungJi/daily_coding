'''
<프로그래머스 카펫>
Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

carpet.png

Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.
'''

# 내 풀이
def solution(brown, yellow):
    answer = []
    total = yellow + brown
    for i in range(3, int(total**0.5)+1):
        if total % i == 0:
            long = max(i, total/i)
            short = min(i, total/i)
            if (long - 2)*(short - 2) == yellow:
                answer.append(long)
                answer.append(short)
                return answer
    return answer
'''
최대 range를 제곱근으로 만든 내 자신이 조금 뿌듯ㅎㅎ
'''

# 다른이 풀이
def solution(brown, yellow):
    w = (brown / 2) + 1
    h = 1
    while w >= h:
        if (w - 2) * (h - 2) == yellow:
            return [w, h]
        w -= 1
        h += 1

'''
왕 이방식 좀 신박ㅎㅎ
'''

# 다른이 풀이
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]
'''
둘레길이로 푸는 방법!
이 방법도 신박ㅎㅎ
'''