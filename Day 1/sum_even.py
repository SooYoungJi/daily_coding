'''
<프로그래머스 짝수의 합>
정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.
'''

# 내 풀이
def solution(n):
    answer = 0
    for i in range(n+1):
        if i%2==0:
            answer+=i
    return answer

# 다른이 풀이1
def solution(n):
    return sum([i for i in range(2, n + 1, 2)])

'''
<memo>
짝수만 출력하기 : range(2, n+1, 2)
sum : 리스트 내 모두 합
'''

# 다른이 풀이2
def solution(n):
    return 2*(n//2)*((n//2)+1)/2

'''
와...이렇게도 풀 수 있구나...
이건 마지 수학 예술 행위...
'''

# 다른이 풀이3
def solution(n):
    return sum(filter(lambda v: v % 2 == 0, [_ for _ in range(n+1)]))

'''
filter 쓴게 신기해서 가져와봤어여(?)
'''