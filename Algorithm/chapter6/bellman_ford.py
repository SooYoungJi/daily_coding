def bellman_ford(edges, num_v):
    dist = [float('inf') for i in range(num_v)]     # 초기값으로 무한대를 설정
    dist[0] = 0

    changed = True

    while changed:      # 비용이 갱신되는 동안 반복
        changed = False
        for edge in edges:  # 각 변을 반복
            if dist[edge[1]] > dist[edge[0]] + edge[2]:
                # 정점까지의 비용을 갱신할 수 있으면 갱신
                dist[edge[1]] = dist[edge[0]] + edge[2]
                changed = True
    return dist

# 변의 리스트(출발점, 끝점, 비용의 리스트)
edges = [
    [0, 1, 4], [0, 2, 3], [1, 2, 1], [1, 3, 1],
    [1, 4, 5], [2, 5, 2], [4, 6, 2], [5, 4, 1],
    [5, 6, 4]
]

print(bellman_ford(edges, 7))