'''
<프로그래머스 문자열 정렬하기(2)>
영어 대소문자로 이루어진 문자열 my_string이 매개변수로 주어질 때, 
my_string을 모두 소문자로 바꾸고 알파벳 순서대로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.
'''

# 내 풀이
def solution(my_string):
    answer = []
    for i in my_string:
        if i.isupper():
            answer.append(i.lower())
        else: 
            answer.append(i)
    answer.sort()
    return ''.join(answer)

# 다른이 풀이1
def solution(my_string):
    return ''.join(sorted(my_string.lower()))

'''
한줄 코딩
그리고 그냥 .lower()해도 모두 lower로 바꿔준다는 것!
'''

# 다른이 풀이2
def solution(my_string):
    answer = []
    for i in my_string:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            answer.append(chr(ord(i)+32))
        else:
            answer.append(i)
    return ''.join(sorted(answer))

'''
아스키 코드를 이용한 방법이라 메모!
'''