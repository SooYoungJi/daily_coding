'''
<프로그래머스 행렬의 덧셈>
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 
2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
'''

# 내 풀이
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[i])):
            temp.append(arr1[i][j]+arr2[i][j])
        answer.append(temp)
    return answer

# 다른이 풀이1
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer

'''
zip을 이렇게도 사용 할 수 있구만~~
'''

# 다른이 풀이2
def sumMatrix(A,B):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] += B[i][j]

    return A
'''
처음에 시도한 코드인데 두번째 for문에서 범위를 A[0]으로 잡야아한다는 것을 간과하고 index에러가 다른 이유에선 난다고 생각함
'''

# 다른이 풀이3
import numpy as np

def sumMatrix(A,B):
    A_np = np.array(A)
    B_np = np.array(B)
    result = A_np + B_np
    return result.tolist()
'''
Aㅏ...?
numpyㅎㅎ
'''