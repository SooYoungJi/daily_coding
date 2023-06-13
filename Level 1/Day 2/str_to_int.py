'''
<프로그래머스 문자열을 정수로 바꾸기>
문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

제한 조건
s의 길이는 1 이상 5이하입니다.
s의 맨앞에는 부호(+, -)가 올 수 있습니다.
s는 부호와 숫자로만 이루어져있습니다.
s는 "0"으로 시작하지 않습니다.
'''

# 내 풀이
def solution(s):
    return int(s)

# 다른이 풀이1
def strToInt(str): 
    result = 0
    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)
    return result
'''
뒤에서부터 숫자를 읽어와 10의 자릿수만큼 곱해주며 -의 여부에 따라 -1을 곱해주는 방법으로 구한것...!
문제의 취지에 부합하는 풀이인 듯하다.
'''

# 다른이 풀이2
def strToInt(str):
    result = 0
    size=len(str)
    temp = 0
    if str [0] == '-' :
        sign = -1
    else :
        sign = 1
    for i in range(0, size) :
        if str[i] == '1' :
            temp = 1
        elif str[i] == '2' :
            temp = 2
        elif str[i] == '3' :
            temp = 3
        elif str[i] == '4' :
            temp = 4
        elif str[i] == '5' :
            temp = 5
        elif str[i] == '6' :
            temp = 6
        elif str[i] == '7' :
            temp = 7
        elif str[i] == '8' :
            temp = 8
        elif str[i] == '9' :
            temp = 9
        else :
            temp = 0
        for i in range(size-i-1) :
            temp = temp * 10
        result = result + temp
    result = result * sign
    return result
'''
처음에는 굳이?라고 생각했는데
댓글을 보니 처리시간이 오히려 줄었다는!
'''