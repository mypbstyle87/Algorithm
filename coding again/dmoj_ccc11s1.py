line_num = int(input())
count_s = 0
count_t = 0
for i in range(line_num):
    line = input()
    for char in line:
        if char == 's' or char == 'S':
            count_s += 1
        elif char == 't' or char == 'T':
            count_t += 1
        else:
            pass

if count_t <= count_s:
    print('French')
else:
    print('English')
