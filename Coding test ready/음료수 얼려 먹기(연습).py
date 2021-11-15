# n, m 입력받기
n, m = map(int, input().split())

# 지도 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 방향 입력
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# dfs 시뮬레이션
def dfs(x, y):
    if graph[x][y] == 1:
        return False
    # 방문처리
    graph[x][y] = 1
    # 사방에 갈수 있는 곳 있는지 체크, 갈 수 있다면 dfs 재귀
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:  # 갈수 있는 곳이라면
            dfs(nx, ny)  # dfs 재귀 실행
    return True  # 리턴의 indent 위치에 따라 정답 나오거나 안나오거나 함, 주의
    # for 안에 리턴이 들어가면, 4방 모두 체크 불가능할수 있음, 따라서 for 밖에 리턴 True 를 줘야함.


# 각 칸에 물 붓기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)  # 정답 출력
