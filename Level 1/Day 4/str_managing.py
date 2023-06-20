'''
<프로그래머스 문자열 다루기 기본>
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.
'''

# 내 풀이
def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            return True
    return False
    

# 다른이 풀이
def alpha_string46(s):
    return s.isdigit() and len(s) in [4,6]
'''
아..?
'''

# 다른이 풀이
def alpha_string46(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6 
'''
try except문 사용은 처음이라~
'''

# 다른이 풀이
def alpha_string46(s):
    import re
    return bool(re.match("^(\d{4}|\d{6})$", s))
'''
정규식 풀이도 참고참고~
'''

