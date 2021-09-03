# 입력
# 첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
# 두 번째 줄에 놓을 수 있는 막대의 개수(n)
# 세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.
# 1 <= w, h <= 100
# 1 <= n <= 10
# d = 0 or 1
# 1 <= x <= 100-h
# 1 <= y <= 100-w

# 출력
# 모든 막대를 놓은 격자판의 상태를 출력한다.
# 막대에 의해 가려진 경우 1, 아닌 경우 0으로 출력한다.
# 단, 각 숫자는 공백으로 구분하여 출력한다.
w, h = map(int, input().split())
pan = [[0 for _ in range(h)] for _ in range(w)]

n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    if d:
        for k, i in enumerate(pan, start=1):
            if x <= k < x+l:
                i[y-1] = 1
    else:
        for _ in range(l):
            pan[x-1][y-1] = 1
            y += 1

for i in pan:
    print(*i)
