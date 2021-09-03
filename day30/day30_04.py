num = int(input())
ans_list = list(map(str, list(i for i in range(1,num + 1) if i % 3)))
print(' '.join(ans_list))
