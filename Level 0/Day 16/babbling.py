'''
<프로그래머스 옹알이(1)>
머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 
조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다.
문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(babbling):
    answer = 0
    bab = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in bab:
            if j in i:
                i = i.replace(j,' ')
        i = i.replace(' ','')
        if i == '':
            answer += 1
    return answer

'''
replace를 쓰는 법을 알게되어서 써봤는데 100프로 내 실력은 아니지만 내껄로 만들어보는걸로!
'''

# 다른이 풀이1
def solution(babbling):
    c = 0
    for b in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
            if w * 2 not in b:
                b = b.replace(w, ' ')
        if len(b.strip()) == 0:
            c += 1
    return c
'''
두번씩 쓰이지 않도록 *2를 사용!
strip()을 사용해서 ' '를 교체
'''

# 다른이 풀이2
import re

def solution(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    cnt=0
    for e in babbling:
        if regex.match(e):
            cnt+=1
    return cnt

'''
컴파일이라니...

'''