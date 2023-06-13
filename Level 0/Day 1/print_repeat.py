'''
<프로그래머스 문자 반복 출력하기>
문자열 my_string과 정수 n이 매개변수로 주어질 때, 
my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.
'''

# 내 풀이
def solution(my_string, n):
    str_list = list(my_string)
    answer = ''
    for i in range(len(my_string)):
        rep = ''
        for j in range(n):
            rep += str(my_string[i])
        answer += rep
    return answer

# 다른이 풀이 1
def solution(my_string, n):
    return ''.join(i*n for i in my_string)

'''
이쯤되면 join 만능설...
'''

# 다른이 풀이 2
def solution(my_string, n):
    answer = ''

    for c in list(my_string):
        answer += c*n
    return answer

'''
문자열도 *하면 곱으로 더해진다
문자열을 for 문의 iter요소로 쓸 수 있다
체크...
'''