# +와 -를 번갈아 출력하기 1

print('+와 -를 번갈아 출력합니다.')
n= int(input('몇 개를 출력할까요? '))

for i in range(n):
    if i % 2: # 나머지가 0이면(even) +, 나머지가 1이면(0이외 숫자면 true) -
        print('-',end="")
    else:
        print('+',end='')

print()