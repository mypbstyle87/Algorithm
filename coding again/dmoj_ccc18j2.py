space_num = int(input())
yesterday = input()
today = input()
# list_yesterday = [i for i in yesterday]
# list_today = [i for i in today]
count = 0
for index in range(space_num):
    if yesterday[index] == today[index] and yesterday[index] == 'C':
        count += 1

print(count)
