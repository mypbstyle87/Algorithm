n = int(input())
d = [0] * (n + 1)


def make_one(n):
    for i in range(2, n + 1):
        d[i] = d[i - 1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)
    print(d)
    return d[-1]


print(make_one(n))
