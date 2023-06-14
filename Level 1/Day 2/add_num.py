'''
<프로그래머스 자릿수 더하기>
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

제한사항
N의 범위 : 100,000,000 이하의 자연수
'''

# 내 풀이
def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer

# 다른이 풀이1
def sum_digit(number):
    '''number의 각 자릿수를 더해서 return하세요'''
    if number < 10:
        return number

    return number%10 + sum_digit(number//10)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)))

'''
오... 재귀함수...
자릿수를 직접 구하는 것도 문제의 취지에는 더 맞는 것 같기도ㅎㅎ
'''

# 다른이 풀이2
def sum_digit(number):
    return sum([int(i) for i in str(number)])
'''
일종의 내 코드 한줄 코딩
'''