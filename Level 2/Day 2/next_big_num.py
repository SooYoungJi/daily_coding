'''
<프로그래머스 다음 큰 숫자>
자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(n):
    i = 1
    while i >= 1:
        if bin(n+i).count('1') == bin(n).count('1'):
            return n+i
        i += 1

# 다른이 풀이
def nextBigNumber(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n
'''
첫 n의 1의 갯수를 저장하고
while문을 돌리면서 n을 증가시켜주는!
'''

# 다른이 풀이
def nextBigNumber(n):
    one_count = bin(n).count('1')

    for compare_num in range(n+1, 1000001):
        if bin(compare_num).count('1') == one_count:
            break

    return compare_num
'''
이런 방법도 있구만!
'''