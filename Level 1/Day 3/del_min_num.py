'''
<프로그래머스 제일 작은 수 제거하기>
정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 
단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 
예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.
'''

# 내 풀이
def solution(arr):
    if len(arr) <= 1:
        return [-1]
    else:
        arr.pop(arr.index(min(arr)))
        return arr
    
# 다른이 풀이
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]

'''
-1은 어떻게 return 하는거지?
'''

# 다른이 풀이
def rm_small(mylist):
    mylist.remove(min(mylist))
    return mylist
'''
remove를 쓰면 index.로 받아서 pop하지 않아도 되는군!'''