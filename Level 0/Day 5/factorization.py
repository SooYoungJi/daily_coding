'''
<프로그래머스 소인수분해>
소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다. 
예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 따라서 12의 소인수는 2와 3입니다. 
자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(n):
    answer = []
    d = 2
    while(d<=n):
        if n%d == 0:
            answer.append(d)
            n = n/d
        else:
            d += 1
    new_answer = set(answer)
    
    return sorted(new_answer)

'''
소인수분해 방법을 인터넷에 찾아봤으니 완전히 내 실력은 아닌걸로ㅠ
'''

# 다른이 풀이1
def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d += 1
    return answer

'''
set이나 sort 대신에 not in 사용하여 계산 줄이기~~
하지만 내 코드 보니까 꽤나 괜찮은 코드인듯~~
'''