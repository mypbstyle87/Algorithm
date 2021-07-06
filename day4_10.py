# 1부터 n까지 정수의 합 구하기(n값은 양수만 입력받음)

print('1부터 n까지 정수의 합을 구합니다.')
num = int(input('n(양수)의 값을 입력하세요.: '))

while True:
    if num > 0:
        break
    else:
        print("양수를 입력하세요.")
        num = int(input('n(양수)의 값을 입력하세요.: '))
sum = 0

for i in range(1, num+1):
    sum += i

print(f"1부터 {num}까지 합은 {sum}입니다.")
