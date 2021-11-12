# 행렬 가로, 세로 입력받기
col, row = map(int, input().split())

# 모든 행의 자료 입력받기
matrix = []
for i in range(col):
    matrix.append(list(input()))

# 정답 입력받을 행렬 초기화
array = [[0] * row for _ in range(col)]

# 체크해야하는 8방향 정의 하기
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [1, 1, 1, 0, -1, -1, -1, 0]

# for 반복문을 통해 모든 지점에서 8방향 체크
for x in range(col):
    for y in range(row):
        if matrix[x][y] == '*':
            array[x][y] = '*'
            continue
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx >= col or ny >= row or ny < 0:
                continue
            if matrix[nx][ny] == '*':
                array[x][y] += 1

# 정답 출력
for i in range(col):
    for j in range(row):
        print(array[i][j], end="")
    print()
