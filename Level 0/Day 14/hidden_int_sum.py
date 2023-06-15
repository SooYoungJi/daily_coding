'''
<프로그래머스 숨어있는 숫자의 덧셈(2)>
문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. 
my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(my_string):
    answer = 0
    digits = []
    temp = ''
    for i in my_string:
        if i.isdigit():
            temp += i
        elif temp != '':
            digits.append(int(temp))
            temp = ''
            
    if temp != '':
        digits.append(int(temp))
        temp = ''
        
    if len(digits) == 0:
        return 0
    
    return sum(digits)

# 다른이 풀이
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())

'''
이번 풀이는 유독 어렵게 풀어서 다른이 풀이가 눈에 들어온다.
연속된 digit이 아니면 ' '를 넣고 ' '를 기준으로 split하는게 포인트!
'''