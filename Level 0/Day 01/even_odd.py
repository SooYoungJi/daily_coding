'''
<프로그래머스 짝수 홀수 갯수>
정수가 담긴 리스트 num_list가 주어질 때, 
num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
'''

# 내 풀이
def solution(num_list):
    even = 0
    odd = 0
    for i in range(len(num_list)):
        if num_list[i]%2 == 0:
            even += 1
        else:
            odd += 1
    
    answer = []
    answer.append(even)
    answer.append(odd)
    return answer

# 다른이 풀이1
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer
'''
그러네 나머지는 결국 짝수나 홀수냐 문제니...
'''

# 다른이 풀이2
def solution(num_list):
    odd = sum(1 for n in num_list if n % 2)
    return [len(num_list) - odd, odd]
'''
이런 분들은 나무보다 숲을 보는 듯하다
'''

'''
TIL

Think different.
나무보다 숲을 보는 시각이 생겨야한다.

이런 멋드러진 코드들을 볼때면 너무 무기력해지지만...
한편으로는 내가 더 성장한다는 마음으로 배워서 내것으로 만들자ㅏㅏ!!
'''