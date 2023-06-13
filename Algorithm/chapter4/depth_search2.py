'''
<알고리즘 독학 4단원 깊이 우선 탐색 - 후위 순회>
'''

tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14],
        [], [], [], [], [], [], [], []]

def search(pos):
    for i in tree[pos]:
        search(i)
    print(pos, end=' ')

search(0)