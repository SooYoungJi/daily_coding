'''
<프로그래머스 모의고사>
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.
'''

# 내 풀이
def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    temp1, temp2, temp3 = 0, 0, 0
    for i in range(len(answers)):
        if one[i%5] == answers[i]:
            temp1 += 1
        if two[i%8] == answers[i]:
            temp2 += 1
        if three[i%10] == answers[i]:
            temp3 += 1

    if temp1 == max(temp1, temp2, temp3):
        answer.append(1)
    if temp2 == max(temp1, temp2, temp3):
        answer.append(2)
    if temp3 == max(temp1, temp2, temp3):
        answer.append(3)
    return answer

'''
코드가 너무 두서없이 긴가 싶었는데 다른이들 코드 보니까 이정도 길이는 되는구나 싶어 안심...ㅎㅎ
'''

# 다른이 풀이
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

'''
조금 더 어떤 배열이 들어와도 계산할 수 있는 형식으로 작성되어있어 깔끔하게 다가옴!
'''

# 다른이 풀이
def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]
'''
조금 더 깔끔하게 푸는 방법이 있어 가져옴ㅎㅎ
p에 2차원 배열로 넣어놓은게 인상적!
'''

# 다른이 풀이
from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]

'''
cycle은 처음이라...ㅎㅎ
'''