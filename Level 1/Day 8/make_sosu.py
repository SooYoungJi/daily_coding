'''
<프로그래머스 소수 만들기>
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
import itertools

def solution(nums):
    answer = 0
    for i in itertools.combinations(nums, 3):
        sosu = True
        for j in range(2, sum(i)):
            if sum(i) % j == 0:
                sosu = False
        if sosu:
            answer += 1
    return answer

'''
정답은 나왔는데
테스트 케이스에서 꽤 오래 걸리는 테케가 있어서 찝찝스...ㅎㅎ
'''

# 다른이 풀이
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer
'''
boolean을 쓰지 않는 방법!
ㅎㅎ그래도 의미는 비슷ㅎㅎ
'''