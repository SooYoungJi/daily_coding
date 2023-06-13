'''
<프로그래머스 모음 제거>
영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 
문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(my_string):
    answer = []
    rem = 'aeiou'
    for i in range(len(my_string)):
        if my_string[i] not in rem:
            answer.append(my_string[i])
            
    return ''.join(answer)

# 다른이 풀이1
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])
'''
내 풀이를 한줄로 쓰는 법~~^^
'''

# 다른이 풀이2
def solution(my_string):
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
    return my_string
'''
replace 사용법!
'''