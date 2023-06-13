'''
<프로그래머스 중복된 숫자 갯수>
정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, 
array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.
'''

# 내 풀이
def solution(array, n):
    answer = 0
    for i in array:
        if i == n:
            answer += 1
    return answer

'''
앞에서 풀었던 방법대로 str(array).count(str(n))을 시도했으나 통과되지 못한 test case가 있었음
'''

# 다른이 풀이1
def solution(array, n):
    return array.count(n)
'''
아... 굳이 str로 바꿀 필요가 없었던 것이었다...ㅎㅎ
'''