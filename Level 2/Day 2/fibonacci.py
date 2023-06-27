'''
<프로그래머스 피보나치 수열>
피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

예를들어

F(2) = F(0) + F(1) = 0 + 1 = 1
F(3) = F(1) + F(2) = 1 + 1 = 2
F(4) = F(2) + F(3) = 1 + 2 = 3
F(5) = F(3) + F(4) = 2 + 3 = 5
와 같이 이어집니다.

2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.
'''
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def solution(n):
    return fibonacci(n)%1234567
'''
테케에서 런타임 에러남
재귀를 쓰고 싶었는디...
'''

def solution(n):
    F = [0, 1]
    for i in range(2, n+1):
        F.append(F[i-1]+F[i-2])
    return F[n]%1234567
'''
차라리 피보나치 수열을 만들고 시작하는게 런타임 에러가 안나는 구나
'''

# 다른이 풀이
def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, (a+b)%1234567
    return a
'''
오...
다른 풀이들도 보니까 재귀를 쓰는 코드보다 수열을 직접 써내려가는 코드가 많이 통과 되는 듯해 보임!
'''