'''
<프로그래머스 짝지어 제거하기>
짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다. 
먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다. 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다. 
이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다. 
문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요. 
성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.

예를 들어, 문자열 S = baabaa 라면

b aa baa → bb aa → aa →

의 순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다.
'''
# 내 풀이
'''
for문과 while문을 통해 list, pop 또는 replace를 이용한 코드를 사용
그랬더니 시간 초과가 계속 뜸'''

# 참고한 풀이
def solution(s):
    b = []
    for i in s:
        if len(b) == 0:
            b.append(i)
        else:
            if b[-1] == i:
                b.pop()
            else:
                b.append(i)
    if len(b) == 0:
        return 1
    return 0

'''
확실히 스텍이 효육성 강자구나...!
'''

# 다른이 풀이
def solution(s):
    temp = ["",s[0]]

    for i in s[1:]:
        if temp[-1]!=i:
            temp.append(i)
        else:
            temp.pop()

    return 1 if len(temp)==1 else 0

'''
이게 뭐람...
'''