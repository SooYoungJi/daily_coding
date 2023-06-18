'''
<프로그래머스 종이 자르기>
머쓱이는 큰 종이를 1 x 1 크기로 자르려고 합니다. 
예를 들어 2 x 2 크기의 종이를 1 x 1 크기로 자르려면 최소 가위질 세 번이 필요합니다.
'''

# 내 풀이
def solution(M, N):
    answer = (M-1) + (M)*(N-1)
    return answer

# 다른이 풀이1
def solution(M, N):
    return (M * N) - 1