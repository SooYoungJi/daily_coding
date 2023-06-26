'''
<프로그래머스 숫자 짝꿍>
두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다
(단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). 
X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.

예를 들어, X = 3403이고 Y = 13203이라면, X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 
다른 예시로 X = 5525이고 Y = 1255이면 X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다
(X에는 5가 3개, Y에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)
두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(X, Y):
    answer = []
    for i in X:
        if i in Y:
            
            answer.append(i)
    answer.sort(reverse=True)
    if len(answer) == 0:
        return '-1'
    elif answer.count('0') == len(answer) :
        return '0'
    else:
        return ''.join(answer)
    
# 내 풀이
def solution(X, Y):
    answer = []
    for i in X:
        if i in Y:
            Y = Y[:Y.index(i)] + Y[Y.index(i)+1:]
            answer.append(i)
    answer.sort(reverse=True)
    if len(answer) == 0:
        return '-1'
    elif answer.count('0') == len(answer) :
        return '0'
    else:
        return ''.join(answer)
    
'''
왜 계속 일부 테케에서 런타임 에러가 나는지 모르겠네ㅜ
'''
# 내 풀이 (최종)
def solution(X, Y):
    answer = []
    for i in set(list(X)):
        if i in Y:
            temp = min(X.count(i), Y.count(i))
            for j in range(temp):
                answer.append(i)
    answer.sort(reverse=True)
    if len(answer) == 0:
        return '-1'
    elif answer.count('0') == len(answer) :
        return '0'
    else:
        return ''.join(answer)
    
'''
힌트보고 풀었지만ㅎㅎ
'''

# 다른이 풀이
def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer
    
'''
애초에 9부터 0까지 count를 하면 되는구나!
그래두 마지막에 00걸러내는건 방법이 같아서 뿌듯!ㅎㅎ
'''