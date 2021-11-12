# bfs 구현을 위한 deque import
from collections import deque

# n, m 입력받기
n, m = map(int, input().split())

# 맵 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs 세팅
def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4방 체크
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로찾기 공간 벗어난경우 무시
            if nx <= -1 or ny <= -1 or nx >= n or ny >= m:
                continue
            # 괴물인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]


# bfs를 수행한 결과 출력
print(bfs(0, 0))
