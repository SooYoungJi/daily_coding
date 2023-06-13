'''
<프로그래머스 외계행성의 나이>
우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다. 
입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다. 
a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다. 
나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(age):
    alpha_age = []
    while(age!=0):
        temp = age%10
        alpha_temp = chr(97+temp)
        alpha_age.append(alpha_temp)
        age = age//10
    alpha_age.reverse()
    return ''.join(alpha_age)
    
# 다른이 풀이
def solution(age):

    return ''.join([chr(int(i)+97) for i in str(age)])

'''
내가 하고자 했던 것을 더 짧게 구현하는 방법!
str도 iteration이 가능하구나...! 이걸 알았다면 조금 더 짧게 구현 가능했을 듯!
그래도 아스키 코드를 떠올린 나 자신이 조금 뿌듯ㅎㅎ
'''