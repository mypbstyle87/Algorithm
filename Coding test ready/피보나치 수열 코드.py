# 피보나치 함수를 다이나믹 프로그래밍(반복-보텀업)으로 구현
def fibo(x):
    fibo_list = [1] * x
    if x >= 2:
        for i in range(2, x):
            fibo_list[i] = fibo_list[i - 1] + fibo_list[i - 2]
    return fibo_list[x - 1]

print(fibo(99))