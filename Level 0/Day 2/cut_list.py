'''
<프로그래머스 배열 자르기>
정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때, 
numbers의 num1번째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 하도록 solution 함수를 완성해보세요.
'''

# 내 풀이
def solution(numbers, num1, num2):
    answer = []
    for i in range(num1, num2+1):
        answer.append(numbers[i])
    return answer

# 다른이 풀이
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

'''
애초에 범위를 정해서 불러 오는 것.
시간 복잡도가 줄어 들 것 같다는 생각이 든다.
'''