# n번 출력, w개마다 줄바꿈 연습하기

n=int(input('몇번 출력할까요?: '))
w=int(input('몇개마다 줄바꿈할까요?: '))

for i in range(n):
    print('*', end='')
    if i % w == w-1:
        print()

if i % w<w-1:
    print()