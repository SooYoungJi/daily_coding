'''
<프로그래머스 다음에 올 숫자>
등차수열 혹은 등비수열 common이 매개변수로 주어질 때, 
마지막 원소 다음으로 올 숫자를 return 하도록 solution 함수를 완성해보세요.
'''

# 내 풀이
def solution(common):
    answer = 0
    if common[2] - common[1] == common[1] - common[0]:
        answer = common[-1] + common[1] - common[0]
    elif common[2] // common[1] == common[1]//common[0]:
        answer = common[-1] * common[1]//common[0]
    return answer

# 다른이 풀이
def solution(common):
    answer = 0
    a,b,c = common[:3]
    if (b-a) == (c-b):
        return common[-1]+(b-a)
    else:
        return common[-1] * (b//a)
    return answer
'''
변수에 배정을 하고 계산을 하면 코드가 훤씬 깔끔하다!
'''