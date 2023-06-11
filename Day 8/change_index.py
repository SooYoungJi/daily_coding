'''
<프로그래머스 인덱스 바꾸기>
문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, 
my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.
'''

# 내 풀이
def solution(my_string, num1, num2):
    str_list = [i for i in my_string]
    temp = str_list[num1]
    str_list[num1] = str_list[num2]
    str_list[num2] = temp
    return ''.join(str_list)

# 다른이 풀이1
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)
'''
swap 사용! 파이썬이라는 것을 잊지 말지!
'''