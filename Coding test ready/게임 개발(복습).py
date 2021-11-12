# 가로, 세로 size 입력받기
col, row = map(int, input().split())

# 현재 위치, 방향 입력받기(x,y,방향)
x, y, direction = map(int, input().split())

# 지도 입력받기
land = []
for _ in range(col):
    land.append(list(map(int, input().split())))

# 북, 서, 남, 동 순으로 단위 좌표 설정
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 지나간 길을 기록하는 배열 0으로 초기화
array = [[0] * row for _ in range(col)]
array[x][y] = 1  # 밟은 자리 1로 만들기


# 왼쪽으로 도는 동작 함수로 만들기
def turn_left():
    global direction
    direction += 1
    if direction == 4:
        direction = 0


# 시뮬레이션
count = 1  # 밟은 장소의 갯수 누적 변수
turn_count = 0  # 왼쪽으로 돌은 횟수(누적 4회면 한바뀌 다 돌았다는 뜻)
while True:
    turn_left()  # 왼쪽으로 돌고
    # 해당 좌표로 가상 이동
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 육지이면서, 가본적도 없다면
    if land[nx][ny] == 0 and array[nx][ny] == 0:
        x, y = nx, ny  # 실제로 좌표 이동
        count += 1  # 밟은 횟수 누적
        turn_count = 0  # 돌은 횟수 초기화
        array[x][y] = 1  # 밟은 자리 1로 만들기
        continue
    else:
        turn_count += 1
    # 제자리에서 한바뀌 다 돈 경우
    if turn_count == 4:
        # 현재 방향에서 뒤쪽으로 가상 이동
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤가 육지면 뒤로 한걸음 걷고, 이후 종료
        if land[nx][ny] == 0:
            x, y = nx, ny
        break

# 정답 출력
print(count)
