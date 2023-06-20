'''
<알고리즘 독학 문제 1>
버킷 정렬은 빈 정렬(bin sort)이라고도 불리며, 값의 종류가 한정된 경우에 사용됩니다.
예를 들어 0 ~ 9의 정수(10종류의 값)만으로 구성된 데이터를 정렬할 때, 각 값이 나오는 횟수만큼 저장하면 됩니다.
다음과 같은 데이터가 주어지면 배열에 해당 값의 발생 횟수를 저장해 작은 순서로 꺼냅니다.
이를 구현하는 프로그램을 작성하세요.
'''

# 내 풀이
data = [9, 4, 5, 2, 8, 3, 7, 8, 3, 2, 6, 5, 7, 9, 2, 9]

count = [0]*10
result = []
def bin_sort(data):
    for i in data:
        count[i] += 1
    for i in range(len(count)):
        result.append([i]*count[i])

    return result 
    
print(bin_sort(data))

# 정답
data = [9, 4, 5, 2, 8, 3, 7, 8, 3, 2, 6, 5, 7, 9, 2, 9]

# 횟수를 저장할 리스트
result = [0] * 10

for i in data:
    # 횟수를 셈
    result[i] += 1

# 결과 출력
for i in range(10):
    for j in range(result[i]):
        print(i, end=' ')