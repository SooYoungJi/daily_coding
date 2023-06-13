'''
<프로그래머스 문자열 안에 문자열>
문자열 str1, str2가 매개변수로 주어집니다. 
str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2

# 다른이 풀이1
def solution(str1, str2):
    return 1 if str2 in str1 else 2

'''
한줄 코딩
'''

# 다른이 풀이2
def solution(str1, str2):
    return 1 + int(str2 not in str1)
'''
True False를 1과 0으로 생각한 것이 신박ㅎㅎ
'''