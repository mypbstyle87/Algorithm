array = list(map(int, input().split()))
min_value = 0
max_value = max(array)
ans_list = [0] * (max_value + 1)
for i in array:
    ans_list[i] += 1

for k, v in enumerate(ans_list):
    for _ in range(v):
        print(k, end=' ')

