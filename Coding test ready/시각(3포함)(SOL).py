# H를 입력받기
h = int(input())

count = 0
for hour in range(0, h + 1):
    for min in range(0, 60):
        for sec in range(0, 60):
            time_str = str(hour) + str(min) + str(sec)
            if '3' in time_str:
                count += 1
print(count)
