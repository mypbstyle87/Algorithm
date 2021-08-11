# 1,000이하의 소수를 나열하기
# 2 제외 짝수는 소수 아니므로 제외(개선)
# n보다 작은 소수로만 나누면 되므로 소수 리스트 내의 원소로만 나눔(개선)

import math
counter = 0
prime = [2]

for n in range(3, 1001, 2):
    for i in prime[1:]:
        counter += 1
        if n % i == 0:
            break
    else:
        prime.append(n)

for i in prime:
    print(i)
print(f'나눗셈을 수행한 횟수 : {counter}')
print(f'소수의 갯수 : {len(prime)}')
