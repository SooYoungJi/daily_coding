'''
<프로그래머스 가장 큰 수 찾기>
정수 배열 array가 매개변수로 주어질 때, 
가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
'''

# 내 풀이
def solution(array):
    num = max(array)
    answer = []
    for i in range(len(array)):
        if array[i] == num:
            answer.append(num)
            answer.append(i)
    return answer

# 다른이 풀이1

def solution(array):
    return [max(array), array.index(max(array))]

'''
index를 추출할 수 이쓴ㄴ 함수가 있었다!
'''