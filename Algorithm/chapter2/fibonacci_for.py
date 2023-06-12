'''
<알고리즘 독학 2단원>
피보나치 수열 반복문 활용
'''

def fibonacci(n):
    fib = [1, 1]

    for i in range(2, n):
        fib.append(fib[i-2] + fib[i-1])

    return fib[n - 1]

print(fibonacci(10))