'''
<프로그래머스 최대값 만들기(1)>
정수 배열 numbers가 매개변수로 주어집니다. 
numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(numbers):
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    return max1*max2
'''
테스트 풀이에서 런타임 에러가 계속 나서 코드를 수정하고 줄였는데 
오히려 다른 방법을 생각해볼 수 있는 과정이라 좋았다!
'''

# 다른이 풀이1
def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]
'''
아... 왜 이생각을 못했지ㅜㅜ
'''

# 다른이 풀이2
def solution(numbers):
    return sorted(numbers)[-1] * sorted(numbers)[-2]
'''
자매품...ㅎㅎ
'''
