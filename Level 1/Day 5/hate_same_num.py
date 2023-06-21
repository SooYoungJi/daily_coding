'''
<프로그래머스 같은 숫자는 싫어>
배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 
이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 
단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 

예를 들면,
arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.
'''

# 내 풀이
def solution(arr):
    answer = []
    for i in arr:
        if len(answer) == 0 or i != answer[-1]:
            answer.append(i)
    return answer
'''
헿 사람들이 좋아하는 코드 중 하나로 똑같이 풀었당ㅎㅎ
'''


# 다른이 풀이
def no_continuous(s):
    # 함수를 완성하세요
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
'''
a[-1:]은 빈 배열에 써도 가능!
'''