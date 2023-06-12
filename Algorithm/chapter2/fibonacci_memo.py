'''
<알고리즘 독학 2단원>
피보나치 수열 메모이제이션으로 처리속도 향상시키기
'''

memo = {1: 1, 2: 1}

def fibonacci(n):
    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci(n-2) + fibonacci(n-1)

    return memo[n]

print(fibonacci(8))