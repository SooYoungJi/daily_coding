'''
<프로그래머스 이상한 문자 만들기>
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
'''

# 내 풀이
def solution(s):
    answer = ''
    s_list = list(s)
    word = s.split(' ')
    now = -1
    for i in word:
        temp = []
        temp = list(i)
        for j in range(len(temp)):
            if j % 2 == 0:
                if temp[j].islower():
                    temp[j] = temp[j].upper()
            else:
                if temp[j].isupper():
                    temp[j] = temp[j].lower()
        answer += ''.join(temp)
        now += len(temp)
        while now+1 <= len(s_list)-1 and s_list[now+1] == ' ':
            now += 1
            answer += ' '
    return answer

'''
나도 내가 복잡하게 푼거 알아...
'''

# 다른이 풀이
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

'''
이렇게 푸는구나...?
생각해보니 사이의 공백을 ' '.join 왜 생각 못했는지이ㅣㅣ
근데 사이의 공백 갯수는 어떻게 했지??
'''

# 다른이 풀이
def solution(s):
    answer = ''
    for word in s.split(" "):
        n = ''
        for i in range(len(word)):
            if i%2 == 0 :
                n += word[i].upper()
            else :
                n += word[i].lower()
        answer += (n + " ")
    return answer[0:-1]

'''
이 풀이는 공백갯수까지 통과!
그러나 어째서...?
'''

# 내 풀이
def solution(s):
    answer_list = []
    word = s.split(' ')
    for i in word:
        temp = list(i)
        for j in range(len(temp)):
            if j % 2 == 0:
                if temp[j].islower():
                    temp[j] = temp[j].upper()
            else:
                if temp[j].isupper():
                    temp[j] = temp[j].lower()
        answer_list.append(''.join(temp))
    return ' '.join(answer_list)
'''
s.split(' ')
' '.join을 하면 공백의 갯수도 포함이 된다는 사실을 깨닫고 고쳐본 풀이
'''