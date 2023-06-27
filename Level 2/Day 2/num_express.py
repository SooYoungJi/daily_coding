'''
<프로그래머스 숫자의 표현>
Finn은 요즘 수학공부에 빠져 있습니다. 
수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 
예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15
자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.
'''

# 내 풀이
def solution(n):
    answer = 0
    for i in range(n, 0, -1):
        temp = 0
        while temp < n and i > 0:
            temp += i
            i -= 1
            if temp == n:
                answer += 1
                break
    return answer
'''
효율성 검사 있길래 런타임에러 걸릴까봐 조마조마 했는데 다행히 통과~~
'''

# 다른이 풀이
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])
'''
역시 수학은 이길 수가 없네...
'''

# 다른이 풀이
def expressions(num):
    answer = 0
    for i in range(1, num+1):
        summ = 0
        while (summ < num):
            summ += i
            i += 1
        if summ == num:
            answer += 1
    return answer
'''
대부분은 이렇게도 푸는군!
'''