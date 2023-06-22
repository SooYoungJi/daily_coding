'''
<프로그래머스 가운데 글자 가져오기>
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 
단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
'''

# 내 풀이
def solution(s):
    if len(s)%2 == 0:
        return s[len(s)//2-1:len(s)//2+1]
    else:
        return s[len(s)//2]


# 다른이 풀이
def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2 + 1]
'''
짝수면 하나 전에 index부터 다음 index까지, 홀수면 가운데 index만 출력된다!
'''

# 다른이 풀이
def string_middle(str):
    a = len(str)
    if a % 2 == 0 :
        a = (a-2) / 2
    else :
        a = (a-1) / 2
    return str[int(a) : -int(a)]
'''
두번쨰 범위를 -int로 하는게 똑똑스'''