'''
<프로그래머스 올바른 괄호>
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 
예를 들어

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 
올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.'''

# 내 풀이
def solution(s):
    answer = True
    open_ = 0
    for i in s:
        if i == "(":
            open_ += 1
        elif i == ")":
            open_ -= 1
        
        if open_ < 0:
            return False
    if open_ == 0:    
        return True
    else:
        return False
    
# 다른이 풀이
def is_pair(s):
    pair = 0
    for x in s:
        if pair < 0: break
        pair = pair + 1 if x == "(" else pair - 1 if x == ")" else pair
    return pair == 0

'''
0과 같은지 아닌지를 이용해 true false를 출력!
'''

# 다른이 풀이
def is_pair(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0
'''
아 pop!
그래서 스택문제였구나!
'''

# 다른이 풀이
def solution(s):
    stack = []
    for i in s:
        # 스택이 비어있는데 닫힌괄호 들어오는 경우 False return
        if len(stack) == 0 and i == ')':
            return False

        # 스택 맨 위에 열린괄호 있는데 닫힌괄호 들어오는 경우: pop
        if i == ')' and stack[-1] == '(':
            stack.pop()

        # 열린 괄호 들어오는 경우 stack에 append
        if i == '(':
            stack.append('(')

    # 다 끝났는데 남아있으면 False return
    return False if len(stack) != 0 else True
'''
이것도!
'''