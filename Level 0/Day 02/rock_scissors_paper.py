'''
<프로그래머스 가위 바위 보>
가위는 2 바위는 0 보는 5로 표현합니다. 
가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때, 
rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.
'''

# 내 풀이
def solution(rsp):
    answer = ''
    for i in rsp:
        if i == '2':
            answer+='0'
        elif i == '0':
            answer+='5'
        else:
            answer += '2'

    return answer
'''
좋지도 나쁘지도 않은듯
'''

# 다른이 풀이1
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)
'''
긋 아이디아...
'''

# 다른이 풀이2
def solution(rsp):
    rsp =rsp.replace('2','s')
    rsp =rsp.replace('5','p')
    rsp =rsp.replace('0','r')
    rsp =rsp.replace('r','5')
    rsp =rsp.replace('s','0')
    rsp =rsp.replace('p','2')
    return rsp

'''
복잡해보이지만 깔끔하면서 의미까지 담은 코딩
'''