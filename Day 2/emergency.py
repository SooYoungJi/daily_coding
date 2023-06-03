'''
<프로그래머스 진료 순서 정하기>
외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다. 
정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(emergency):
    #dict를 이용하면 편할듯
    max = len(emergency)
    em_dict = dict()
    for i in range(1, max+1):
        em_dict[i] = emergency[i-1]
    
    sorted_dict = sorted(em_dict.items(), key = lambda item: item[1], reverse = True)
    sorted_list = [[0]*2 for _ in range(max)]
    for i in range(max):
        sorted_list[i][0] = i+1
        sorted_list[i][1] = sorted_dict[i][1]
    
    em_num = []
    for i in range(max):
        for j in range(max):
            if emergency[i] == sorted_list[j][1]:
                em_num.append(sorted_list[j][0])

    return em_num

'''
힘든 싸움이었다...ㅎㅎ하ㅏㅏㅎ하ㅏ하
'''
# 다른 이 풀이1
def solution(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]

'''
이 코드를 보기 위해 나의 긴 코드를 짰다고 해도 과언이 아닐 정도...
'''