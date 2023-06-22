'''
<프로그래머스 2016년>
2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 
두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 
요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT

입니다. 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.
'''

# 내 풀이
def solution(a, b):
    days = 1
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN', 'MON']
    days += sum(month[:a])
    days += b+1
    return day[days%7]

'''
사실 조금 꺼림직ㅎㅎ
아... 이제껏 1월1일은 화요일이라 생각하고 풀고 있었음... 그래서 계속 안맞았구나...
'''

def solution(a, b):
    days = 0
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    days += sum(month[:a])
    days += b-1
    return day[days%7]

'''
내 풀이 바꿔서 다시 풀었음ㅎ
'''

# 다른이 풀이
def getDayName(a,b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return day[(sum(month[:a-1])+b-1)%7]
'''
내 풀이와 비슷!
'''