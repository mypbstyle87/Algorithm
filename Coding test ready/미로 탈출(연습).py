from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque([(x, y)])
    while queue: # while 사용 익숙해질것
        x, y = queue.popleft() # 튜플이므로 자동 언패킹
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1: # 항상 최대 탐색공간 밖으로 나가는지 체크할것
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1 # 길일때만 경로 누적 할수 있는 방법
    return graph[n - 1][m - 1]


print(bfs(0, 0))
