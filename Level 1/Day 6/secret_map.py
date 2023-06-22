'''
<프로그래머스 비밀지도>
네오는 평소 프로도가 비상금을 숨겨놓는 장소를 알려줄 비밀지도를 손에 넣었다. 
그런데 이 비밀지도는 숫자로 암호화되어 있어 위치를 확인하기 위해서는 암호를 해독해야 한다. 
다행히 지도 암호를 해독할 방법을 적어놓은 메모도 함께 발견했다.

지도는 한 변의 길이가 n인 정사각형 배열 형태로, 각 칸은 "공백"(" ") 또는 "벽"("#") 두 종류로 이루어져 있다.
전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다. 각각 "지도 1"과 "지도 2"라고 하자. 
지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다. 
지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
"지도 1"과 "지도 2"는 각각 정수 배열로 암호화되어 있다.
암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.'''

# 내 풀이
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp = 0
        temp = bin(arr1[i] | arr2[i])[2:]
        temp = temp.replace('1', '#')
        temp = temp.replace('0', ' ')
        if len(temp) <= n-1:
            temp = ' '*(n-len(temp)) + temp
        answer.append(temp)
    return answer
'''
자릿수가 맞지 않을 때 공백을 채우는게 약간의 고비였음
조금 더 깔끔하게 공백을 고려하는 방법이 궁금함
'''

# 다른이 풀이
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
'''
rjust라는 함수가 있나보다^^
그것 빼고는 푸는 방법이 비슷한듯!

<rjust>
오른쪽으로 정렬하도록 도와준다.
rjust를 통해 공백의 수, 공백을 메워줄 문자를 넣어준다.

val = "77".rjust(5, "0")
print(val)
>>00077

<ljust>
왼쪽으로 정렬하도록 도와준다.
ljust를 통해 공백의 수, 공백을 메워줄 문자를 넣어준다.

val = "222".ljust(15, "a")
print(val)
>>222aaaaaaaaaaaa

<zfill>
이는 0을 왼쪽에 채워주는 역할을 한다.

val = "2".zfill(3)
print(val)
>>002
'''