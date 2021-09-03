# 3,6,9 게임

num = int(input())
list_369 = [3, 6, 9]

for i in range(1, num + 1):
    num_10, num_1 = divmod(i, 10)
    if num_10 in list_369 and num_1 in list_369:
        print('XX')
        continue
    if num_10 in list_369:
        print('X')
        continue
    if num_1 in list_369:
        print('X')
        continue
    print(i)

n = int(input())

for i in range(1, n+1) :
  if i%10==3 or i%10==6 or i%10==9 :
    print("X", end=' ')
  else :
    print(i, end=' ')