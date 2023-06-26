'''
<프로그래머스 JadenCase>
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 
단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.'''

# 내 풀이
def solution(s):
    answer = []
    s_list = s.split(" ")
    for i in s_list:
        if i != '':
            i = i.replace(i[0], i[0].upper())
            i = i.replace(i[1:], i[1:].lower())
        if i == '':
            answer.append('')
        else: 
            answer.append(i)
    return " ".join(answer)

'''
공백이 여러개일때를 고려하지 못함
'''