cur_position = input()
count = 0
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
num_list = ['1', '2', '3', '4', '5', '6', '7', '8']

x = alpha_list.index(cur_position[0])
y = num_list.index(cur_position[1])

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or ny < 0 or nx > 7 or ny > 7:
        continue
    count += 1
print(count)
