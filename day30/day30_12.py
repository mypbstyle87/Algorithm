# 개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직였다.
# (오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다.)

# 이에 호기심이 생긴 영일이는 그 개미를 미로 상자에 넣고 살펴보기 시작하였다.

# 미로 상자에 넣은 개미는 먹이를 찾았거나, 더 이상 움직일 수 없을 때까지
# 오른쪽 또는 아래쪽으로만 움직였다.

# 미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
# 먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.

# 단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
# 더이상 이동하지 않고 그 곳에 머무른다고 가정한다.

# 미로 상자의 테두리는 모두 벽으로 되어 있으며,
# 개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.

inp_list = []
for _ in range(10):
    temp_list = list(map(int, input().split()))
    inp_list.append(temp_list)
next_num = 0
x, y = 1, 1
inp_list[x][y] = 9
while True:
    if inp_list[x][y + 1] == 1:
        x += 1
    else:
        y += 1
    next_num = inp_list[x][y]
    inp_list[x][y] = 9
    if next_num == 2 or (inp_list[x][y + 1] == 1 and inp_list[x + 1][y] == 1):
        break

for i in inp_list:
    print(*i)
