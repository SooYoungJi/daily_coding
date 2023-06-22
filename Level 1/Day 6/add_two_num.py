'''
<프로그래머스 두 개 뽑아서 더하기>
정수 배열 numbers가 주어집니다. 
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 
배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
'''

import itertools

def solution(numbers):
    answer = []
    for i in itertools.combinations(numbers, 2):
        if i[0]+i[1] not in answer:
            answer.append(i[0]+i[1])
    return sorted(answer)

'''
itertools 안쓰고도 for문으로 할수도 있을 것 같기는 함
'''

# 다른이 풀이
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))
'''
내가 말한 for문!
안그래도 set 생각나기는 했는데
set으로 바뀌었다가 list로 바꾸는게 list안에 확인하고 선별해서 추가하는 것보다 시간이 적게 걸릴까?
'''