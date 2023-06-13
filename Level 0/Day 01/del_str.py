'''
<프로그래머스 특정 문자 제거>
문자열 my_string과 문자 letter이 매개변수로 주어집니다. 
my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(my_string, letter):
    str_list = list(my_string)
    ans_str=[]
    for i in str_list:
        if i != letter:
            ans_str.append(i)
    answer = ''.join(ans_str)
    return answer

'''
코드는 길었지만 이전 문제에서 계속 활용 못하던 join을 활용해서 조금 신남ㅎㅎ
'''

# 다른이 풀이1

def solution(my_string, letter):
    return my_string.replace(letter, '')

'''
.replace(대체 대상, 대체자)
memo...
'''

# 다른이 풀이2

def solution(my_string, letter):
    return ''.join([c for c in my_string if c != letter])

'''
리스트로 꼭 변환 안해도 for문에서 str iteration이 가능하다!
'''