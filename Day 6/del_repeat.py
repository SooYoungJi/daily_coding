'''
<프로그래머스 중복된 문자 제거>
문자열 my_string이 매개변수로 주어집니다. 
my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(my_string):
    answer=[]
    for i in my_string:
        if i not in answer:
            answer.append(i)
    return ''.join(answer)

'''
set을 이용해 풀어보려했으나 set은 순서가 랜덤으로 저장된다는 것을 깨닫고 
순서가 있어야 하는 문제였어서 list를 이용했다.
'''

# 다른이 풀이
def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer+=i
    return answer
'''
내 풀이와 다른점은 나는 리스트를 이용해 join을 하므로 계산을 한번 더 늘렸다는 것.
바로 string에 붙이는 법이 있다니!
'''

# 다른이 풀이2
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))

'''
set가 아닌 dict를 사용했으면 내가 원하는 코드를 구현 할 수 있었겠다!
'''