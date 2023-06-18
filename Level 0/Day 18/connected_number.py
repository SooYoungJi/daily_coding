'''
<프로그래머스 연속된 수의 합>
연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 두 정수 num과 total이 주어집니다. 
연속된 수 num개를 더한 값이 total이 될 때, 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.
'''

# 내 풀이
def solution(num, total):
    for i in range(total//num-num, total//num+num):
        if sum([j for j in range(i, i+num)]) == total:
            answer = [j for j in range(i, i+num)]
    return answer

'''
다른 테스트 케이스에서 런타임 에러가 나서 
처음 검색 range()를 최소한으로 줄어 보았더니 해결이 되었다.
'''

# 다른이 풀이
def solution(num, total):
    # base
    # offset
    # # sum of offsets = num(num-1) / 2
    base = total - num * (num-1) / 2
    base = int(base // num)
    answer = [i for i in range(base, base+num)]
    return answer

'''
수학적으로 접근!
'''