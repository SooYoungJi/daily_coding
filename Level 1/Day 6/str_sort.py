'''
<프로그래머스 문자열 내 마음대로 정렬하기>
문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 
예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.
'''

# 내 풀이
def solution(strings, n):
    for j in range(len(strings)):
        for i in range(1, len(strings)):
            if strings[i-1][n] > strings[i][n]:
                strings[i-1], strings[i] = strings[i], strings[i-1]
            elif strings[i-1][n] == strings[i][n]:
                if strings[i-1] > strings[i]:
                    strings[i-1], strings[i] = strings[i], strings[i-1]

    return strings

'''
for문을 두번이나 돌리는게 조금 마음에 걸리지만...
'''

# 다른이 풀이
def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=lambda x: (x[n], n))

'''
아... sorted로 기준을 주면 되는구나...?
'''

# 다른이 풀이
def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    def sortkey(x):
        return x[n]
    strings.sort(key = sortkey)
    return strings
'''
이런 방법도 있구만?? 
하지만 이 코드는 더이상 n번째 문자가 같을 때 사전순으로 배열하지 못한다.
'''