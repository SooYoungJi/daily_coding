'''
<프로그래머스 최댓값과 최솟값>
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 
"(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.
'''

# 내 풀이
def solution(s):
    answer = ''
    list_s = s.split(' ')
    int_s = []
    for i in list_s:
        int_s.append(int(i))
    int_s.sort()
    return str(int_s[0])+' '+str(int_s[-1])

'''
뭔가 int로 list를 바로 만드는 법이 있을듯!
'''

# 다른이 풀이
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))

'''
아... 이거네ㅎㅎ
'''

# 다른이 풀이
def solution(s):
    s_list=s.split(" ")
    n = [int(i) for i in s_list]
    n.sort()

    return str(n[0]) + " " + str(n[len(n)-1])
'''
아 []안에서 바꿔버리는 방법도 있군!'''