n = int(input())
score_list = []
for _ in range(n):
    name, score = tuple(input().split())
    score_list.append((int(score), name))

sorted_list = sorted(score_list)
for i in sorted_list:
    print(i[1], end=' ')
