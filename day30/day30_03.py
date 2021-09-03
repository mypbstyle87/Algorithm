# rgb 계산 (itertools)

import itertools

a, b, c = map(int, input().split())
list_a = list(range(a))
list_b = list(range(b))
list_c = list(range(c))

temp = list(itertools.product(list_a, list_b, list_c))
for i in temp:
    print(*i)
print(len(temp))