'''
<프로그래머스 자릿수 더하기>
정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요
'''

# 내 풀이
def solution(n):
    return sum([int(i) for i in str(n)])

'''
코드를 한줄로 줄여보고 다양한 함수를 쓰려는 노력을 했고 그런 부분 실력이 조금 오른 기분!
'''

# 다른이 풀이1
def solution(n):
    return sum(int(i) for i in str(n))
'''
굳이 list로 안만들어도 되었음! 
'''

# 다른이 풀이2
def solution(n):
    answer = 0
    while n:
        answer += n%10
        n //= 10
    return answer
'''
자릿수 개념으로 접근했다는 것이 인상적!
'''