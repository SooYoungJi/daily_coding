'''
<프로그래머스 약수의 합>
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
'''

# 내 풀이
def solution(n):
    return sum([i for i in range(1, n+1) if n%i == 0])

'''
저번에 제곱근 값구해서 그 밑에 구하고 두배하던거 사용해보고 싶었는데 기억이 잘 나지 않아서 내가 할 수 있는 최선...
'''

# 다른이 풀이1
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
'''
아마도 이게 내가 하고 싶었던 것 같다.
'''

