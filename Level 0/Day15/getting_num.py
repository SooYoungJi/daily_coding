'''
<프로그래머스 유한소수 판별하기>
소수점 아래 숫자가 계속되지 않고 유한개인 소수를 유한소수라고 합니다. 
분수를 소수로 고칠 때 유한소수로 나타낼 수 있는 분수인지 판별하려고 합니다. 유한소수가 되기 위한 분수의 조건은 다음과 같습니다.

기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다.

두 정수 a와 b가 매개변수로 주어질 때, a/b가 유한소수이면 1을, 무한소수라면 2를 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(a, b):
    for i in range(1, a+1):
        if a%i == 0 and b%i == 0:
            a /= i
            b /= i
    while b%2==0:
        b/=2
    while b%5==0:
        b/=5
    
    if b==1:
        return 1
    else:
        return 2
    
'''
점점 구성력이 무너지는 코드가 되어 가는 것 같아 슬프지만...
'''

# 다른이 풀이1
from math import gcd
def solution(a, b):
    b //= gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2

'''
확실히 gcd를 사용했구만...
그래도 그것 말고는 코드 구성이 많이 벗어나지 않음!
'''