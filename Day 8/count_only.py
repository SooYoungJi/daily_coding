'''
<프로그래머스 한 번만 등장한 문자>
문자열 s가 매개변수로 주어집니다. 
s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요. 
한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.
'''

# 내 풀이
def solution(s):
    s_dict = dict()
    answer = []
    for i in s:
        if i in s_dict.keys():
            s_dict[i] += 1
        else:
            s_dict[i] = 1
    for i in s_dict.keys():
        if s_dict[i] == 1:
            answer.append(i)
    answer.sort()
    return ''.join(answer)

# 다른이 풀이 1
def solution(s):
    answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
    return answer

'''
count() 함수!
'''