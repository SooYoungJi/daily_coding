'''
<프로그래머스 문자열 뒤집기 문제>
문자열 my_string이 매개변수로 주어집니다. 
my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(my_string):
    my_list = list(my_string)
    my_list.reverse()
    answer = str(my_list[0])
    for i in range(len(my_list)-1):
        answer += str(my_list[i+1])
    return answer

# 다른이 풀이1
def solution(my_string):
    return my_string[::-1]

# 다른이 풀이2
def solution(my_string):
    my_list = list(my_string)
    my_list.reverse()
    answer = ''.join(my_list)
    return answer

''' 
<TIL>

    문자열[::-1]
    ''.join() 

활용하는 법을 배웠다
'''