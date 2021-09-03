# num = int(input(),16)
# print('{0:o}'.format(num))

# (a,) = map(int, input().split())
# print('a: ', a)

# love 3
# a, b = map(int, input().split())
# print(type(divmod(a, b)),divmod(a,b))

import itertools

a = [1, 2, 3, 4, 5, 6]
for i in (list(itertools.product(a, a))):
    print(*i)

num = int(input(), 16)
for i in range(1, 16):
    print('{0:X}*{1:X}={2:X}'.format(num, i, num * i))

