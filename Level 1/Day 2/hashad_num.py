'''
<프로그래머스 하샤드 수>
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 
예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 
자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.
'''

# 내 풀이
def solution(x):
    hashad = 0
    for i in str(x):
        hashad += int(i)
    if x % hashad == 0:
        return True
    return False

# 다른이 풀이1
def Harshad(n):
    return n%sum(int(x) for x in str(n)) == 0

'''
Sum함수를 이렇게 쓸 수 있군! 
시도하려했으나 사용법을 명확히 알지 못하면 활용을 못한다는 것을 잊지말기!
'''