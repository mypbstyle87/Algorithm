# a, b 를 공백으로 구분하여 입력 받기
a, b = map(int, input().split())

# x좌표, y좌표, 방향을 공백으로 구분하여 입력 받기
x_cord, y_cord, direction = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
footprint_list = [[0] * b for _ in range(a)]
footprint_list[x_cord][y_cord] = 1  # 현재 좌표 방문 처리

# 전체 맵 정보 입력 받기
mat = []
for _ in range(b):
    mat.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 설정
dx = [-1, 0, +1, 0]
dy = [0, +1, 0, -1]


# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x_cord + dx[direction]
    ny = y_cord + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if mat[nx][ny] == 0 and footprint_list[nx][ny] == 0:
        footprint_list[nx][ny] = 1
        x_cord, y_cord = nx, ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x_cord - dx[direction]
        ny = y_cord - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if footprint_list[nx][ny] == 0:
            x_cord, y_cord = nx, ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)
