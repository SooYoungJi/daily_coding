'''
<프로그래머스 직사각형 별찍기>
이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.
'''
# 내 풀이
a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print("*", end = '')
    print("", end = "\n")


# 다른이 풀이1
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)

'''
아 그르네...ㅎ
'''

# 다른이 풀이2
a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print('*', end='')
    print('')

'''
굳이 /n안해도 되는구나...?
'''

# 다른이 풀이 3
a, b = map(int, input().strip().split(' '))
for _ in range(b):
    print('*'*a)
'''
이런 풀이도 있담ㅎㅎ
'''