'''
<프로그래머스 구슬을 나누는 경우의 수>
머쓱이는 구슬을 친구들에게 나누어주려고 합니다. 구슬은 모두 다르게 생겼습니다. 
머쓱이가 갖고 있는 구슬의 개수 balls와 친구들에게 나누어 줄 구슬 개수 share이 매개변수로 주어질 때, 
balls개의 구슬 중 share개의 구슬을 고르는 가능한 모든 경우의 수를 return 하는 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(balls, share):
    temp1 = 1
    temp2 = 1
    for i in range(balls-share+1, balls+1):
        temp1 *= i
    for j in range(1, share+1):
        temp2 *= j
    answer = temp1/temp2
    return answer

# 다른이 풀이1
import math


def solution(balls, share):
    return math.comb(balls, share)

'''
그랬다. math에 조합이 있었다...
'''

# 다른이 풀이2
def solution(balls, share):
    answer = factorial(balls) / (factorial(balls - share) * factorial(share))
    return answer

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

'''
팩토리얼을 직접 구현한 함수
사실 생각을 안해본건 아니다ㅎㅎ
'''