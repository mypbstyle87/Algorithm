n = int(input())
store = list(map(int, input().split()))

d = [0] * n
d[0] = store[0]
d[1] = max(d[0], store[1])

for i in range(2, n):
    d[i] = max(store[i] + d[i - 2], d[i - 1])

print(max(d))