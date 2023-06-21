'''
<프로그래머스 3진법 뒤집기>
자연수 n이 매개변수로 주어집니다. 
n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
'''

# 배경지식
'''
<int 사용 (n진수 to 10진수)>
int(수, base(n진수))

<함수 작성(10진수 to n진수)>
def solution(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1]  # 가장 작은 수부터 입력했기 때문에 역순으로 바꿔줘야 원하는 숫자를 얻을 수 있음
    '''

# 내 풀이
def solution(n):
    rev = ''
    while n > 0:
        n, mod = divmod(n, 3)
        rev += str(mod)
    return int(rev, 3)

'''
위의 코드를 참고하여 풀이
'''

# 다른이 풀이
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer
'''
순서가 조금 다를 뿐 별반 다르지 않음
'''

# 다른이 풀이
def solution(n):
    answer = 0
    cnt = 1
    a = ''
    while n>0:
        a+=str(n%3)
        n = n//3
    print(a)
    for b in range(len(a),0,-1):
        answer += (int(a[b-1])*cnt)
        cnt *= 3
    return answer
'''
3진수 수를 10진수로 바꾸는 과정까지 구현한 풀이
'''