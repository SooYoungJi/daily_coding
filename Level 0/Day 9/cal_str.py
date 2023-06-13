'''
<프로그래머스 문자열 계산하기>
my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 
문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(my_string):
    answer = 0
    string_list = my_string.split(' ')
    answer = int(string_list[0])
    for i in range(2, len(string_list), 2):
        if string_list[i-1] == '+':
            answer += int(string_list[i])
        elif string_list[i-1] == '-':
            answer -= int(string_list[i])
    return answer

'''
단항식이 아닌 다항식의 경우를 고려하여 작성
'''

# 다른이 풀이1
solution=eval

'''
ㅎㅎㅎ eval...메모...
'''

# 다른이 풀이2
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))
'''
- 부호를 + - 로 바꾸어 모두 sum하는 방법!
'''
