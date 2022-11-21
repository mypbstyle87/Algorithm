def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1


num, targ = input().split()
num = int(num)
arr = input().split()

print(sequential_search(num, targ, arr))
