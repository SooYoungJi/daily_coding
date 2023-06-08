'''
<프로그래머스 대문자 소문자>
문자열 my_string이 매개변수로 주어질 때, 
대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            answer+=i.lower()
        else:
            answer+=i.upper()
    return answer

'''
한줄 코딩...있겠지...
'''

# 다른이 풀이(띵풀이)
def solution(my_string):
    return my_string.swapcase()
'''
이런 함수가 있었냐고,,,
'''

# 다른이 풀이(...라 쓰고 한줄코딩이라 읽는ㄷr...)
def solution(my_string):
    return ''.join([x.lower() if x.isupper() else x.upper() for x in my_string])
'''
아마도 내가 원했던 한줄코딩...
'''
