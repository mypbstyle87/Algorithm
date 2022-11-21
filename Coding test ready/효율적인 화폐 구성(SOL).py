n, m = map(int, input().split())
d = [10001] * (m + 1)  # 초기화
cur_list = []
for _ in range(n):
    cur_list.append(int(input()))  # 화폐 가치 리스트로 입력

d[0] = 0

for i in range(n):
    for j in range(cur_list[i], m + 1):
        d[j] = min(d[j], d[j - cur_list[i]] + 1)

print(d[m])
