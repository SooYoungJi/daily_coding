'''
<프로그래머스 가까운 수>
정수 배열 array와 정수 n이 매개변수로 주어질 때, 
array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(array, n):
    diff = dict()
    for i in array:
        if i-n < 0:
            diff[i] = -(i-n)
        else: 
            diff[i] = i-n
    min_diff = min(diff.values())
    answers = [int(k) for k, v in diff.items() if v==min_diff]
    return min(answers)

'''
첫 풀이는 차이 값이 같을 때 가장 작은 수를 답으로 꺼내오는 것을 적용하지 못해서 다시 작성한 코드인데 아주 쏙 마음에 들지 않는다...
'''

# 다른이 풀이1
solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]

'''
오... 와...
일단 abs 메모... 절댓값 만들어주는 코드를 알아냈다ㅎㅎ
근데 코드만 보고는 이해가 바로 되지는 않는다...
'''

def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer

'''
그리고 바로 밑에 이런 풀이가 있었다. 
이해가 조금 더 잘 된다

~참고용 댓글~
abs(x-n), x-n) 값을 두 개 넣어주신 이유를 알 수 있을까요?
ㄴ sort key 값에 2개 항목을 넣을 수 있어요. 첫번째 정렬, 두번째 정렬인데 x-n을 넣어주는 이유는 abs(x-n)이 똑같은 경우 값 작은게 앞에 있게 하려고요. 제한에 보시면 거리가 같은경우 작은 값을 가져오라 했거든용
'''

def solution(array, n):
    return sorted([(abs(a - n), a) for a in array])[0][1]

'''
이 코드가 조금 더 직관적인듯!
'''