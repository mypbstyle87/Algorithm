def fibo(x):
    d = [1] * x

    for i in range(2, x):
        d[i] = d[i - 2] + d[i - 1]

    return d[-1]

print(fibo(400))
