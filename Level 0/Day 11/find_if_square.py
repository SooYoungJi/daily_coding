'''
<프로그래머스 제곱수 구하기>
어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 
정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
import math
def solution(n):
    n_r = math.sqrt(n)
    return 1 if n%n_r == 0 else 2

'''
math import은 좀 꼼수 같은가...?ㅎㅎㅎ
'''

# 다른이 풀이1
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2
'''
0.5승은 좀 기발했다.
'''