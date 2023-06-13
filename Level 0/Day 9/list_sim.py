'''
<프로그래머스 배열 유사도>

'''

# 내 풀이
def solution(s1, s2):
    answer = 0
    for i in s1:
        for j in s2:
            if i==j:
                answer += 1
    return answer


# 다른이 풀이1
def solution(s1, s2):
    return len(set(s1)&set(s2))

'''
set으로 만든 후 교집합의 길이를 구하는 방식! 시간 복잡도 감소!
'''

# 다른이 풀이2
def solution(s1, s2):
    answer = 0

    for word in s1:
        if word in s2:
            answer += 1
        else:
            continue

    return answer
'''
이것도 나의 풀이보다는 시간 복잡도가 줄어 들어서 참고용으로 좋다!
'''