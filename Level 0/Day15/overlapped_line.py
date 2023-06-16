'''
<프로그래머스 겹치는 선분의 길이>
선분 3개가 평행하게 놓여 있습니다. 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때, 
두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.

lines가 [[0, 2], [-3, -1], [-2, 1]]일 때 그림으로 나타내면 다음과 같습니다.

line_2.png

선분이 두 개 이상 겹친 곳은 [-2, -1], [0, 1]로 길이 2만큼 겹쳐있습니다.
'''

# 내 풀이
def solution(lines):
    
    answer = 0
    bubble = 0
    max_num = max(sum(lines,[]))
    min_num = min(sum(lines,[]))
    
    if min_num < 0:
        bubble = abs(min_num)
    
    overlap = [0 for _ in range(max_num+bubble+1)]
    
    for i in lines:
        for j in range(i[0], i[1]+1):
            overlap[j+bubble] += 1
    
    for i in range(min_num, max_num+1):
        if overlap[i-1] > 1 and overlap[i] > 1:
            answer += 1

    return answer

'''
테케 몇개가 안풀림

넘무 어렵다아ㅏㅏ..
'''

def solution(lines):
    
    answer = 0
    bubble = 0
    max_num = max(sum(lines,[]))
    min_num = min(sum(lines,[]))
    
    if min_num < 0:
        bubble = abs(min_num)
    
    overlap = [0 for _ in range(max_num+bubble+1)]
    
    for i in lines:
        for j in range(i[0], i[1]):
            overlap[j+bubble] += 1
    
    for i in range(min_num, max_num+1):
        if overlap[i] > 1:
            answer += 1

    return answer
'''
풀어따아ㅏㅏㅏㅏ
'''

# 다른이 풀이
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])

'''
이렇게 간단한 방법이...ㅎㅎㅎ
'''