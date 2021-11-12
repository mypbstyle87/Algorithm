count = 0
ans = 0
for i in range(1, 61):
    if '3' in str(i):
        count += 1

n = int(input())

quo, res = divmod(n, 10)

if res >= 3:
    ans = (n - quo) * 1575 + (quo + 1) * 3600
else:
    ans = (n + 1 - quo) * 1575 + quo * 3600
print(ans)