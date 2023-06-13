'''
<프로그래머스 잘라서 배열로 저장하기>
문자열 my_str과 n이 매개변수로 주어질 때, 
my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(my_str, n):
    answer = []
    i = 0
    while i<len(my_str):
        answer.append(my_str[i:i+n])
        i += n
    return answer

# 다른이 풀이1
def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]

'''
while 보다 더 나은지는 모르겠지만
range를 쓰고 step을 n으로 하므로 i += n을 생략 할 수 있음
'''
