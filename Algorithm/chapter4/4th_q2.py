'''
<알고리즘 독학 4단원 예제2>
도시를 3개 선탣하여 인구의 합계가 500만에 가장 가까운 조합과 그 인구를 구하세요.
'''

# 목푯값
goal = 5000000

# 각 도시의 인구
pref = [3416918, 1525849, 1147037, 1044579, 828947, 654963, 565392, 506494, 2925967, 1496172, 1068641, 942649,
        818760, 652845, 542713, 489202, 2453041, 1193894, 1061440, 840047, 702545, 650599, 521642]

# 500만 명에 가까운 인구 수
min_total = 0

# 두 지역의 인구 수를 저장하는 임시 변수
local_temp = 0

# 지역 1~3 인구 수의 인덱스를 저장
local_index1 = 0
local_index2 = 0
local_index3 = 0

def search(total, pos):
    global min_total, local_temp, local_index1, local_index2, local_index3
    if pos >= len(pref):
        return
    if total < goal:
        if abs(goal - (total + pref[pos]) < abs(goal - min_total)):
            min_total = total + pref[pos]
            local_temp = total
            local_index1 = pos
        search(total + pref[pos], pos + 1)
        search(total, pos + 1)
    for local_index2 in range(22):
        for local_index3 in range(22):
            if local_temp - pref[local_index2] == pref[local_index3]:
                break
        break

search(0, 0)
print(min_total)
print(pref[local_index1])
print(pref[local_index2])
print(pref[local_index3])