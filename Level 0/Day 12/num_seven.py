'''
<프로그래머스 7의 개수>
머쓱이는 행운의 숫자 7을 가장 좋아합니다. 
정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.
'''

# 내 풀이
def solution(array):
    answer = 0
    for i in array:
        answer += str(i).count('7')
    return answer


# 다른이 풀이1
def solution(array):
    return str(array).count('7')

'''
내 풀이를 조금 더 간단히 한...!
str(리스트)를 하면 그냥 str 전체가 되는구나!
'''

