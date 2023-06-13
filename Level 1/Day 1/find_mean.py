'''
<프로그래머스 평균 구하기>
정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.
'''

# 내 풀이1

import numpy as np

def solution(arr):
    return np.mean(arr)

'''
살짝 꼼수 같아서 다른 코드도 짜보았다.
'''

# 내 풀이2

def solution(arr):
    return sum(arr)/len(arr)
