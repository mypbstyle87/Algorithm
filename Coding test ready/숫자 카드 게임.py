col, row = map(int, input().split())
mat = []
for _ in range(col):
    mat.append(min(list(map(int, input().split()))))

print(max(mat))