'''<프로그래머스 정수 내림차순으로 배치하기>
함수 solution은 정수 n을 매개변수로 입력받습니다. 
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 
예를들어 n이 118372면 873211을 리턴하면 됩니다.
'''

# 내 풀이
def solution(n):
    answer = [i for i in str(n)]
    answer.sort(reverse=True)
    return int(''.join(answer))

# 다른이 풀이1
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))
'''
그냥 str로 바꿔서 list 씌우면 되는 것이었다...ㅎㅎ
'''

# 다른이 풀이2

2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] >= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def solution(n):
    arr = list(str(n))
    n = int(''.join(mergeSort(arr)))
    return n
'''
sort를 함수로 만들어 버리는 멋짐...
'''