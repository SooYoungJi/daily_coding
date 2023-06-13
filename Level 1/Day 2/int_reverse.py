'''
<프로그래머스 자연수 뒤집어 배열로 만들기>
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 
예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
'''

# 내 풀이
def solution(n):
    answer = [int(i) for i in str(n)]
    answer.reverse()
    return answer

# 다른이 풀이1
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
'''
오호라... reversed(str(n))이라니!
map과 list도 자유롭게 쓰면 이렇게 할 수 있구나!
'''