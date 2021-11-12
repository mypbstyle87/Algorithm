# dfs로 풀겠어

# 입력 받기
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


# dfs 세팅(재귀 사용)
def dfs(x, y):
    if x >= n or y >= m or x < 0 or y < 0:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
