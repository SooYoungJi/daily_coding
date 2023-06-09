'''
<프로그래머스 저주의 숫자 3>
3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 3의 배수와 숫자 3을 사용하지 않습니다. 3x 마을 사람들의 숫자는 다음과 같습니다.

10진법	3x 마을에서 쓰는 숫자	10진법	3x 마을에서 쓰는 숫자
1	            1	        6	        8
2	            2	        7	        10
3	            4	        8	        11
4	            5	        9	        14
5	            7	        10      	16
정수 n이 매개변수로 주어질 때, n을 3x 마을에서 사용하는 숫자로 바꿔 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(n):
    shift = []
    shift.append(0)
    while len(shift)>0:
        temp = 0
        for i in range(1, n+shift[-1]+1):
            if i % 3 == 0 or '3' in str(i):
                temp += 1
        shift.append(temp)
        if shift[-1] == shift[-2]:
            break
    return n+shift[-1]
'''
나름 생각 잘했다고 생각함
'''

# 댜른이 풀이1
def solution(n):
    answer = [0, 1, 2, 4, 5, 7, 8, 10, 11, 14, 16, 17, 19, 20, 22, 25, 26, 28, 29, 40, 41, 44, 46, 47, 49, 50, 52, 55, 56, 58, 59, 61, 62, 64, 65, 67, 68, 70, 71, 74, 76, 77, 79, 80, 82, 85, 86, 88, 89, 91, 92, 94, 95, 97, 98, 100, 101, 104, 106, 107, 109, 110, 112, 115, 116, 118, 119, 121, 122, 124, 125, 127, 128, 140, 142, 145, 146, 148, 149, 151, 152, 154, 155, 157, 158, 160, 161, 164, 166, 167, 169, 170, 172, 175, 176, 178, 179, 181, 182, 184, 185]
    return answer[n]
'''
이건 광기다...
'''

# 다른이 풀이2
def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer

'''
내가 원했던게 이런 풀이 일수도...? 아이디어는 같았으나 여기가 조금 더 세련되었다...ㅎㅎ
'''