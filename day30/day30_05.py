a, b, c = map(int, input().split())
for i in range(1, 1000000):
    if i % a == 0 and i % b == 0 and i % c == 0:
        print(i)
        break