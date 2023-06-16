'''
<프로그래머스 특이한 정렬>
정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다. 이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 
정수가 담긴 배열 numlist와 정수 n이 주어질 때 numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(numlist, n):
    num_dict = []
    for i in numlist:
        num_dict.append([abs(n-i), i])
    num_dict.sort(key=lambda x:(x[0], -x[1]))
    return [i[1] for i in num_dict]

'''
2차원 배열을 sort하는 법을 찾아봤지만 앞으로도 잘 이용해보는 걸로!
'''

# 다른이 풀이
def solution(numlist, n):
    return sorted(numlist,key = lambda x: [abs(x-n),-x])
'''
차잇값이 작은 순서대로, 나머지는 값이 더 큰 순서대로...!!
'''