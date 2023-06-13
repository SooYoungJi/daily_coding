'''
<프로그래머스 x만큼 간격이 있는 n개의 숫자>
함수 solution은 정수 x와 자연수 n을 입력 받아, 
x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다.
다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

제한 조건
x는 -10000000 이상, 10000000 이하인 정수입니다.
n은 1000 이하인 자연수입니다.
'''

# 내 풀이
def solution(x, n):
    answer = []
    i = x
    while len(answer)<n:
        answer.append(i)
        i += x
    return answer

# 다른이 풀이1
def number_generator(x, n):
    # 함수를 완성하세요
    return [i * x + x for i in range(n)]
print(number_generator(2, 5))

'''
생각해보니 range(n)을 사용해 곱한건 좀 똑똑한듯
'''

# 다른이 풀이2
def number_generator(x, n):
    # 함수를 완성하세요
    return [i for i in range(x, x*n+1, x)]
print(number_generator(2,5))

'''
이것도 생각 안한건 아닌데 마지막 range숫자를 지정하는 방식이 조금 지저분 하다고 생각했음
그러나 막상 보니까 나쁘지 않은듯!
'''