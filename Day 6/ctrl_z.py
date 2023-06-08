'''
<프로그래머스 컨트롤 제트>
숫자와 "Z"가 공백으로 구분되어 담긴 문자열이 주어집니다. 문자열에 있는 숫자를 차례대로 더하려고 합니다. 
이때 "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다. 
숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.
'''

# 내 풀이
def solution(s):
    answer = 0
    s_list = s.split(' ')
    last = 0
    for i in s_list:
        if i == 'Z':
            answer -= last
        else:
            answer += int(i)
            last = int(i)
    return answer


# 다른이 풀이1
def solution(s):
    answer = 0
    for i in range(len(s := s.split(" "))):
        answer += int(s[i]) if s[i] != "Z" else -int(s[i-1])
    return answer
'''
풀이 방법은 같으나 한줄쓰기한 버전!
'''

# 다른이 풀이2
def solution(s):
    stack = []
    for a in s.split():
        if a != 'Z':
            stack.append(int(a))
        else:
            if stack:
                stack.pop()

    return sum(stack)
'''
신박한 풀이!
'''