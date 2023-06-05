'''
<프로그래머스 배열 회전시키기>
정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다. 
배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(numbers, direction):
    answer = []
    temp = []
    if direction == 'right':
        temp = numbers[:-1]
        answer.append(numbers[-1])
        for i in temp:
            answer.append(i)
    else:
        answer = numbers[1:]
        answer.append(numbers[0])
    return answer

# 다른이 풀이1
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]
'''
1. 배열을 더하면 순서대로 더해진다!
2. 나와 같은 코드 한줄로 요약한것임
'''

# 다른이 풀이2
from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)
'''
deaue 함수에 있는 rotate 사용
'''