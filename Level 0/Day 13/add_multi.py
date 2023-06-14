'''
<프로그래머스 다항식 더하기>
한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 
덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 
같은 식이라면 가장 짧은 수식을 return 합니다.
'''

# 내 풀이
def solution(polynomial):
    answer_x = 0
    answer_int = 0
    poly = polynomial.split(' ')
    for i in poly:
        if i[-1] == 'x':
            if len(i) == 1:
                answer_x += 1
            else:
                answer_x += int(i[:-1])
        elif i != '+':
            answer_int += int(i)
    answer = []
    if answer_x > 0:
        if answer_x == 1:
            answer.append('x')
        else:
            answer.append(str(answer_x)+'x')
    if len(answer) != 0 and answer_int != 0:
        answer.append('+')
    if answer_int > 0:
        answer.append(str(answer_int))

    return ' '.join(answer)

'''
조금 지저분,,,ㅎㅎ
'''

# 다른이 풀이1
def solution(polynomial):
    xnum = 0
    const = 0
    for c in polynomial.split(' + '):
        if c.isdigit():
            const+=int(c)
        else:
            xnum = xnum+1 if c=='x' else xnum+int(c[:-1])
    if xnum == 0:
        return str(const)
    elif xnum==1:
        return 'x + '+str(const) if const!=0 else 'x'
    else:
        return f'{xnum}x + {const}' if const!=0 else f'{xnum}x'
    
'''
split을 ' + '로 사용하는 방법!
str인 상태에서도 isdigit()을 판별할 수 있구나!
return 할때 f'{}'사용하는 방법!
'''