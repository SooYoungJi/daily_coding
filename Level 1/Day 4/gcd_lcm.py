'''
<프로그래머스 최대공약수와 최소공배수>
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 
예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.
'''

# 내 풀이
import math
def solution(n, m):
    gcds = math.gcd(n, m)
    lcm = m*n//gcds
    return [gcds, lcm]

'''
gcd를 직접 구했을면 좋았을 듯!
'''

# 다른이 풀이
def gcdlcm(a, b):
    c,d = max(a, b), min(a, b)
    t = 1
    while t>0:
        t = c%d
        c, d = d, t
    answer = [ c, int (a*b/c)]
    return answer
'''
최대공약수를 구하는 법!
c,d = max(a, b), min(a, b)
t = 1
while t>0:
    t = c%d
    c, d = d, t

최소공배수를 구하는 법!
두 수의 곱을 최대공약수로 나눈다!
'''