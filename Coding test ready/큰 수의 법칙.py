n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort(reverse=True)
count, rest = divmod(m, (k + 1))
num_sum = count * num_list[0] * k + count * num_list[1] + rest * num_list[0]
print(num_sum)
