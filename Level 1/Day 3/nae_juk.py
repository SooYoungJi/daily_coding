'''
<프로그래머스 내적>
길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. 
a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.

이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다.
(n은 a, b의 길이)
'''

# 내 풀이
def solution(a, b):
    return sum(i*j for i, j in zip(a, b))

'''
헤헤 1등 풀이랑 같당ㅎㅎ
'''