'''
<프로그래머스 숫자 찾기>
정수 num과 k가 매개변수로 주어질 때, 
num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 
없으면 -1을 return 하도록 solution 함수를 완성해보세요.
'''

# 내 풀이
def solution(num, k):
    t = 0
    for i in str(num):
        t+=1
        if int(i) == k:
            return t
    return -1

# 다른이 풀이1
def solution(num, k):
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1

'''
str().find를 사용했으면 더 쉬웠을 것 같다.
'''
