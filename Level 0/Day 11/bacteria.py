'''
<프로그래머스 세균 증식>
어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 
처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(n, t):
    answer = n
    for i in range(t):
        answer*=2
    return answer

# 다른이 풀이1
def solution(n, t):
    return n << t
'''
아... 비트연산...ㅎㅎ하하ㅏㅏ
'''

# 다른이 풀이2
def solution(n, t):
    answer = 2**t * n
    return answer
'''
나의 풀이를 조금 더 똑똑하게 작성ㅎㅎ 시간 복잡도가 줄어들 것 같다.
'''