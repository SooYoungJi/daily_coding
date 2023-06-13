'''
<프로그래머스 문자열 정렬하기(1)>
문자열 my_string이 매개변수로 주어질 때, 
my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.
'''

# 내 풀이
def solution(my_string):
    answer = [int(i) for i in my_string if i in '0123456789']
    answer.sort()
    return answer
'''
나름 리스트 안에서 조건 실행하는 한줄 표현 써서 뿌듯ㅎㅎ
'''

# 다른이 풀이1
def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])
'''
sorted...
isdigit()...
메모...
'''