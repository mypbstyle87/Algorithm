# n, m 입력받기 n: 화폐 종류 수, m: 목표 금액
n, m = map(int, input().split())

# 화폐 종류별로 입력받기
array = []
for _ in range(n):
    array.append(int(input()))

# dp 초기화
d = [10001] * (m + 1)
d[0] = 0

# 보텀업 다이나믹 프로그래밍 구현
for i in range(n):
    for j in range(array[i], m + 1):
        d[j] = min(d[j - array[i]] + 1, d[j])

# 문제 제한조건 수행
if d[m] == 10001:
    print(-1)
else:
    print(d[m])