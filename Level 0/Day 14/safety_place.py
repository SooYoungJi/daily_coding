'''
<안전지대>
다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.
'''

# 내 풀이
def solution(board):
    answer = 0
    bomb = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                bomb.append([i, j])
    if len(bomb) == 0:
        return len(board)*len(board[0])
    else:
        for i in bomb:
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if (0 <= i[0]+k < len(board)) & (0 <= i[1]+l < len(board[0])):
                        board[i[0]+k][i[1]+l] = 1

    for i in range(len(board)):
        answer += board[i].count(0)

    return answer

'''
다소 많이 복잡했던 나의 풀이...
'''

# 다른이 풀이1
def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)

'''
set으로 update하며 [-1, 0, 1]을 사용하여 더한 방법,
전체에서 danger한 부분만 뺀 방식!
'''

# 다른이 풀이2
def solution(board):
    answer = 0

    for col in range(len(board)):
        for row in range(len(board[col])):
            if board[row][col] == 1:
                for j in range(max(col-1,0),min(col+2,len(board))):
                    for i in range(max(row-1,0),min(row+2,len(board))):
                        if board[i][j] == 1:
                            continue
                        board[i][j] = -1
    for i in board:
        answer += i.count(0)

    return answer

'''
min과 max를 이용하여 범위를 벗어나지 않는 방식!
'''