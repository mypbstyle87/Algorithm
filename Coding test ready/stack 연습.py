# factorial 구하기(for)

# n = int(input())
# ans = 1
# for i in range(1, n + 1):
#     ans *= i
#
# print(ans)

# factorial 구하기(recursive function)

n = int(input())
ans = 1
def recursive_factorial(n):
    if n == 1:
        return 1
    return n * recursive_factorial(n - 1)
print(recursive_factorial(n))
