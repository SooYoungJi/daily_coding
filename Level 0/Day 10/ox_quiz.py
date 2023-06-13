'''
<프로그래머스 ox 퀴즈>
덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다. 
수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(quiz):
    answer = []
    for i in quiz:
        cal = i.split(' ')
        
        if eval(''.join(cal[:3])) == int(cal[-1]):
            answer.append("O")
        else:
            answer.append("X")
        
    return answer

# 다른이 풀이1
def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]    

'''
= 부호를 == 부호로 교체하므로써 진짜 OX퀴즈의 취지에도 맞고 깔끔한 코드를 만들었다...
'''

# 다른이 풀이2
def solution(quiz):
    answer = []
    for q in quiz:
        p, a = q.split("=")
        if eval(p) == int(a):
            answer.append("O")
        else:
            answer.append("X")
    return answer

'''
'='부호를 기점으로 split하는 것도 좋다!
변수 두개를 놓고 split을 하면 앞의 것은 앞의 변수에, 뒤의 것은 뒤의 변수에 저장 된다는 팁 메모!
'''