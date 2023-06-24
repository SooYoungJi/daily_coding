'''
<프로그래머스 소수 찾기>
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)
'''

# 내 풀이1
def solution(n):
    answer = 0
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            answer += 1
    return answer

'''
테스트 케이스 시간초과...
'''

# 내 풀이2
def solution(n):
    sosu = [2]
    for i in range(2, n+1):
        for j in sosu:
            if i % j == 0:
                break
        else:
            sosu.append(i)
    return len(sosu)
'''
이것도 시간초과...? ㅜㅜ
'''

# 내 풀이 + 알고리즘 교재의 에라토스테네스의 체
import math

def solution(n):
    if n == 2:
        return 1
    prime = [2]
    limit = int(math.sqrt(n))
    
    data = [i+1 for i in range(2, n, 2)]
    
    while limit >= data[0]:
        prime.append(data[0])
        data = [j for j in data if j%data[0] != 0]
    
    return len(prime + data)

'''
n==2일때를 고려하지 않아서 
효율성에서 넘어가도 
테케 1번에서 에러가 났었음...
'''

# 다른이 풀이
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

'''
아 이렇게도 간단히 할 수 있구나?
꼭 limit을 걸지 않아도..ㅎㅎ
아 찾아보니 효율성에서 좋은 코드는 아니라고 함
'''