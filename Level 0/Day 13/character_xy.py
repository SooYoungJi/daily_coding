'''
<프로그래머스 캐릭터의 좌표>
머쓱이는 RPG게임을 하고 있습니다. 
게임에는 up, down, left, right 방향키가 있으며 각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동합니다. 
예를 들어 [0,0]에서 up을 누른다면 캐릭터의 좌표는 [0, 1], down을 누른다면 [0, -1], left를 누른다면 [-1, 0], right를 누른다면 [1, 0]입니다. 
머쓱이가 입력한 방향키의 배열 keyinput와 맵의 크기 board이 매개변수로 주어집니다. 
캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 캐릭터의 좌표 [x, y]를 return하도록 solution 함수를 완성해주세요.

[0, 0]은 board의 정 중앙에 위치합니다. 
예를 들어 board의 가로 크기가 9라면 캐릭터는 왼쪽으로 최대 [-4, 0]까지 오른쪽으로 최대 [4, 0]까지 이동할 수 있습니다.
'''

# 내 풀이
def solution(keyinput, board):
    answer = [0, 0]
    limit = [i//2 for i in board]
    key = ["up", "down", "left", "right"]
    move = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    for i in keyinput:
        answer[0] += move[key.index(i)][0]
        if abs(answer[0]) > limit[0]:
            answer[0] -= move[key.index(i)][0]
    for j in keyinput:
        answer[1] += move[key.index(j)][1]
        if abs(answer[1]) > limit[1]:
            answer[1] -= move[key.index(j)][1]
    return answer


'''
테스트 코드에서 자꾸 한문제에서 걸려서 넘어가지를 못했음
'''

# 다른이 풀이1
def solution(keyinput, board):
    curr = [0, 0]
    for k in keyinput:
        if k == 'left':
            curr[0] = max(curr[0] - 1, -(board[0] // 2))
        elif k == 'right':
            curr[0] = min(curr[0] + 1, board[0] // 2)
        elif k == 'down':
            curr[1] = max(curr[1] - 1, -(board[1] // 2))
        else:
            curr[1] = min(curr[1] + 1, board[1] // 2)

    return curr
'''
더할때는 min을, 뺄떄는 max를 구하는 아이디어!
'''

# 다른이 풀이2
def solution(keyinput, board):
    x_lim,y_lim = board[0]//2,board[1]//2
    move = {'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
    x,y = 0,0
    for k in keyinput:
        dx,dy = move[k]
        if abs(x+dx)>x_lim or abs(y+dy)>y_lim:
            continue
        else:
            x,y = x+dx,y+dy

    return [x,y]

'''
dictionary를 사용한 부분과 dx, dy에 move[k]로 지정한게 똑똑했다!
'''

