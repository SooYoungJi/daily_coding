'''
<프로그래머스 팩토리얼>
i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다. 
예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다. 
정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.
i! ≤ n
'''

# 내 풀이
def solution(n):
    factorial = 1
    i = 1
    while(factorial<=n):
        i += 1
        factorial *= i

    return i-1

'''
test case가 자꾸 하나가 안돌아가서 고생했지만
for문을 써야하는 때와 while문을 써야하는 때를 구분하는 연습이 되었다.
'''

# 다른이 풀이1
from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k
'''
factorial 함수가 있었다...ㅎㅎ
'''