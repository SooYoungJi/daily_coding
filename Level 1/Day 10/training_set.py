'''
<프로그래머스 체육복>
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 
학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 
예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 
체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 
여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 
체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
'''

# 내 풀이
def solution(n, lost, reserve):
    train = [1] * (n+2)
    train[0] = 0
    train[-1] = 0
    
    for i in reserve:
        train[i] += 1
    for i in lost:
        train[i] -= 1
    for i in range(1, n+1):
        if train[i] == 0:
            if train[i-1] > 1:
                train[i] += 1
                train[i-1] -= 1
            elif train[i+1] > 1:
                train[i] += 1
                train[i+1] -= 1

    return (n+2) - train.count(0)
'''
그 전에 pop을 사용한 방법을 이용했는데 계속 런타임 에러가 났다.
'''

# 다른이 풀이
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
'''
reserve와 lost의 겹치는 부분 없애는 코드
pop이 아닌 remove를 사용하면 런타임 에러가 덜 나나??
생각해보니 그냥 숫자인데 굳이 index를 고집할 필요가 있었나 싶음
reserve에 있는 수를 lost에서 찾으면 lost에서 remove하는게 인상적,
'''

# 다른이 풀이
def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n+1):
        if i not in lost: #안 잃어버린 학생
            answer += 1
        else:
            if i in reserve: #잃어버렸지만 여분도 있는 학생
                answer += 1
                reserve.remove(i)
                lost.remove(i)

    for i in lost: #잃어버리고 여분도 없어서 빌려야 하는 학생
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)

        elif i+1 in reserve:
            answer +=1
            reserve.remove(i+1)

    return answer
'''
아무래도 처음에 pop이 문제였나보다
찾아보니 같은 O(N)인데ㅜㅜ
'''