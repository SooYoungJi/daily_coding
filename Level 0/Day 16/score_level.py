'''
<프로그래머스 등수 매기기>
영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다. 
영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때, 
영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이

import numpy as np

def solution(score):
    answer = []
    mean_score = [np.mean(i) for i in score]
    sorted_score = sorted(mean_score, reverse = True)
    rank = 1
    rank_answer = []
    for i in range(len(sorted_score)):
        if i>0 and sorted_score[i]==sorted_score[i-1]:
            answer.append(answer[i-1])
        else:
            answer.append(rank)
        rank += 1
    for i in range(len(answer)):
        rank_answer.append([answer[i], sorted_score[i]])
        
    real_answer = []
    for i in mean_score:
        for j in rank_answer:
            if i == j[1]:
                real_answer.append(j[0])
                break

    return real_answer

'''
너무 복잡해애ㅐㅐㅐ 분명히 깔끔한 답이 있을 것 같은데에ㅔㅔ
'''

# 다른이 풀이1
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]

'''
숫자 갯수가 같으니 굳이 mean을 구하지 않아도 됨
그냥 index를 갖고와도 중복된 수 일때 앞의 숫자를 갖고 오는구나!
'''

# 다른이 풀이2
def solution(score):
    rank = sorted([sum(s) / 2 for s in score], reverse=True)
    rankDict = {}
    for i, r in enumerate(rank):
        if r not in rankDict.keys():
            rankDict[r] = i + 1
    return [rankDict[sum(s) / 2] for s in score]

'''
역시 dict는 사용하는게!
1. rank는 sorted로 해서 숫자를 순서대로 저장
2. dict에는 처음 발견된 순서로 저장
3. dict에 없으면 index+1로 저장
4. 다시 score 배열로 와서 dict에 저장되어있는 순서로 입력!
'''