'''
<프로그래머스 머쓱이보다 키 큰사람>
머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다. 
머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때, 
머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.
'''

# 내 풀이
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    for i in array:
        if i == height:
            return array.index(i)
        
'''
처음엔 제대로 정렬후 전체 크기에서 height가 가지는 index를 뺐는데 test case에서 실패가 떴음
중복된 키를 가진 사람들을 고려하지 못함.
'''

# 다른이 풀이1
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)

'''
내 풀이와 큰차이 없지만 나는 불필요한 탐샏을 하나 추가 하였음.
그냥 index 바로 뽑으면 되는 거였음
'''

#다른이 풀이2
def solution(array, height):
    return sum(1 for a in array if a > height)

'''
이상적인 답처럼 보임
'''