'''
<알고리즘 2단원>
피보나치 수열
'''

def fibonacci(n):
    if (n ==1) or (n == 2):
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(6))