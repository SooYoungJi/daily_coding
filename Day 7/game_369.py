'''
<프로그래머스 369게임>
머쓱이는 친구들과 369게임을 하고 있습니다. 
369게임은 1부터 숫자를 하나씩 대며 3, 6, 9가 들어가는 숫자는 숫자 대신 3, 6, 9의 개수만큼 박수를 치는 게임입니다. 
머쓱이가 말해야하는 숫자 order가 매개변수로 주어질 때, 머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.
'''

# 내 풀이
def solution(order):
    answer = 0
    for i in str(order):
        if i in '369':
            answer+=1
    return answer
'''
솔직히 내 풀이도 나쁘지 않다고 봄~
'''

# 다른이 풀이1
def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))
'''
하... 자꾸만 map쓰는게 익숙치 않군...
이번 문제는 count를 쓰느느게 관건인 것 같다!
'''

# 다른이 풀이2
def solution(order):
    answer = 0
    order = str(order)
    return order.count('3') + order.count('6') + order.count('9')
'''
깔끔하고 계산량이 많지 않아보이는게 좋은 코드인듯!
'''