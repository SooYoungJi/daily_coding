data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

change = True
for i in range(len(data)):
    if not change:          # 요소교환이 일어나지 않으면 종료
        break
    change = False          # 요소 교환이 발생하지 않았다고 설정
    for j in range(len(data)-i-1):      # 정렬된 부분을 제외하고 반복 실행
        if data[j] > data[j+1]:         # 앞쪽이 큰 경우
            data[j], data[j+1] = data[j+1], data[j]
            change = True

print(data)