'''
<프로그래머스 두 정수 사이의 합>
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
'''

# 내 풀이
def solution(a, b):
    if a>b:
        a, b = b, a
    return sum(i for i in range(a, b+1))

'''
다른이 풀이 가장 맨 위에 올라와 있는 코드와 동일하게 나왔다ㅎㅎ 괜히 뿌듯ㅎㅎ
'''

# 다른이 풀이1
def adder(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))
'''
for문 없이 그냥 range를 sum해도 되는구나!
'''

# 다른이 풀이2
def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2
'''
아...?
이건 걍 수학 머리...ㅎㅎ 수학공부도 열쉬미 해야겠다ㅎㅎ
'''

# 다른이 풀이3
def adder(a, b):
    return sum(range(min(a, b), max(a, b)+1))
'''
min max를 사용하면 교차 선언 안해도 됨ㅎㅎ
'''