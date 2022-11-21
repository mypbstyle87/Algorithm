line = input()
count_h = 0
count_o = 0
count_n = 0
count = 0
for char in line:
    if char == 'H':
        count_h += 1
    if char == 'O' and count_h >= 1:
        count_o += 1
    if char == 'N' and count_o >= 1:
        count_n += 1
    if char == 'I' and count_n >= 1:
        count += 1
        count_h, count_o, count_n = 0, 0, 0
print(count)
