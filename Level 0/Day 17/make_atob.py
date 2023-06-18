'''
<프로그래머스 A로 B 만들기>
문자열 before와 after가 매개변수로 주어질 때, before의 순서를 바꾸어 after를 만들 수 있으면 1을, 
만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.
'''

# 내 풀이
def solution(before, after):
    before_list = list(before)
    after_list = list(after)
    if sorted(before_list) == sorted(after_list):
        return 1
    return 0

# 다른이 풀이1
def solution(before, after):
    before=sorted(before)
    after=sorted(after)
    if before==after:
        return 1
    else:
        return 0
'''
list로 바꾸지 않아도 sort 가능
'''

# 다른이 풀이2
def solution(before, after):
    return 1 if sorted(before)==sorted(after) else 0
'''
한줄 코딩~
'''