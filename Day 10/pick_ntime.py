'''
<프로그래머스 n의 배수 고르기>
정수 n과 정수 배열 numlist가 매개변수로 주어질 때, 
numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
    return answer

# 다른이 풀이1
def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))

'''
filter와 lambda를 적절히 잘 사용하면 깔끔한 코드 작성이 가능하다~'''

# 다른이 풀이2
def solution(n, numlist):
    answer = [i for i in numlist if i%n==0]
    return answer
'''
내가 쓴 코드를 한줄로 쓰면 이렇게 쓸 수 있다~~'''