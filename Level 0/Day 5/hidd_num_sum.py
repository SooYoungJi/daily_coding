'''
<프로그래머스 숨어있는 숫자의 덧셈(1)>
문자열 my_string이 매개변수로 주어집니다. 
my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit():
            answer+=int(i)
    return answer
'''
isdigit() 바로 써먹어서 뿌듯ㅎㅎ
'''

# 다른이 풀이1
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())
'''
아... sum... 한줄풀이~~^^
'''