'''
<프로그래머스 옹알이(2)>
머쓱이는 태어난 지 11개월 된 조카를 돌보고 있습니다. 
조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고 
연속해서 같은 발음을 하는 것을 어려워합니다. 문자열 배열 babbling이 매개변수로 주어질 때, 
머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    #see = []
    for i in babbling:
        compare = ''
        for j in words:
            if j in i:
                if j*2 not in i:
                    compare += j*i.count(j)
        #see.append(compare)
        if len(compare) == len(i):
            answer += 1
    return answer

# 다른이 풀이
def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer
'''
연속된 단어를 배재하는 방법은 같았음
그러나 여기서는 존재하는 단어를 ' '로 replace하고
남은 글자가 없을 때 답으로 체크하도록 되어있다.
'''