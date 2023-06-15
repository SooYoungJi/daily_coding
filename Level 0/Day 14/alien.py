'''
<프로그래머스 외계어 사전>
PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다. 
알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어집니다. 
spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 존재하지 않는다면 2를 return하도록 
solution 함수를 완성해주세요.
'''
# 내 풀이
def solution(spell, dic):
    answer = 0
    test = []
    for i in dic:
        temp = 0
        for j in spell:
            if j in i:
                temp += 1
        if temp == len(spell):
            return 1        
    return 2

'''
문제를 원래보다 어렵게 생각해서 돌아감
'''

# 다른이 풀이1
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2

'''
set의 특성을 너무 잘 사용한 케이스
'''

# 다른이 풀이2
def solution(spell, dic):
    for d in dic:
        if sorted(d) == sorted(spell):
            return 1
    return 2
'''
따로 set을 하지 않아도 되는건가?
'''