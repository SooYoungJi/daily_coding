'''
<프로그래머스 합성수 찾기>
약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 
자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.
'''
# 내 풀이
def lcd(n):
    num = 0
    for i in range(1, n+1):
        if n%i == 0:
            num += 1
    if num > 2:
        return True

def solution(n):
    answer = 0
    for i in range(1, n+1):
        if lcd(i):
            answer += 1
    return answer

# 다른이 풀이1
def solution(n):
    output = 0
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output

'''
어렵다...ㅎㅎ
i까지로 하면 컴파일 시간이 너무 길어지기 때문! 
반복 범위를 줄이기 위해, 대부분 자연수의 약수는 대상의 제곱근 이하의 약수 하나와 이상의 약수 하나씩 한 쌍을 이룬다는 점을 응용해 
i의 제곱근까지 반복하게 한 다음, 4나 9등의 제곱수를 고려해 +1을 해서 예외를 해결한 경우
'''

# 다른이 풀이2
def get_divisors(n):
    return list(filter(lambda v: n % v ==0, range(1, n+1)))

def solution(n):
    return len(list(filter(lambda v: len(get_divisors(v)) >= 3, range(1, n+1))))
'''
filter를 사용하여 한줄코딩을 만들려는 시도...!
계산량을 줄이는 코드가 아닌이상 너무 짧기 위해 만든 코드는 마냥 좋은 코드가 아니라는 생각이 든다.
'''