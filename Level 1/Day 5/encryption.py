'''
<프로그래머스 시저 암호화>
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 
예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 
문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.
'''

def solution(s, n):
    answer = ''
    for i in s:
        if ord('a') <= ord(i) <= ord('z'):
            answer += chr(ord("a") + ((ord(i) + n - ord("a")) % 26))
        elif ord('A') <= ord(i) <= ord('Z'):
            answer += chr(ord("A") + ((ord(i) + n - ord("A")) % 26))
        else:
            answer += i
    return answer

'''
if ord('a') <= ord(i) <= ord('z'):
    answer += chr(ord("a") + ((ord(i) + n - ord("a")) % 26))

chr()
ord()
a~z에서 맴돌게 하려면
시작 알파벳의 아스키 번호 + (문제 알파벳 + 뒤로 밀 숫자 - 시작 알파벳의 아스키 번호)를 전체 a~z갯수로 나눈 나머지
그냥 외워ㅓㅓㅓ
'''

# 다른이 풀이
def caesar(s, n):
    lower_list = "abcdefghijklmnopqrstuvwxyz"
    upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = []

    for i in s:
        if i is " ":
            result.append(" ")
        elif i.islower() is True:
            new_ = lower_list.find(i) + n
            result.append(lower_list[new_ % 26])
        else:
            new_ = upper_list.find(i) + n
            result.append(upper_list[new_ % 26])
    return "".join(result)
'''
정 모르겠으면 이런 방법도 있음!
참고!
'''