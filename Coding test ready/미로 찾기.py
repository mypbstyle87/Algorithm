# bfs로 풀겠어(최단거리니깐)
from collections import deque

# 입력 받기
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 방향(상, 하, 좌, 우) 설정
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]


# bfs 셋팅
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[n - 1][m - 1]


print(bfs(0, 0))
