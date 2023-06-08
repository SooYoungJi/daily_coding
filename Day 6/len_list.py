'''
<프로그래머스 배열 원소의 길이>
문자열 배열 strlist가 매개변수로 주어집니다. 
strlist 각 원소의 길이를 담은 배열을 retrun하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(strlist):
    return [len(i) for i in strlist]

'''
어쩐지 점점 한줄코딩에 집착하게 되는 것 같지만 실력이 느는 것 같아 뿌듯하다ㅎㅎ
'''

# 다른이 풀이1
def solution(strlist):
    answer = list(map(len, strlist))
    return answer

'''
map을 사용했어도 좋은 듯ㅎㅎ
'''