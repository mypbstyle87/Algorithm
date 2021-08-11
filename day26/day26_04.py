# deepcopy! 리스트 내의 리스트 복사시, 참조하는 부분을 복사(얕은 복사)를 하므로, 원 리스트의 값이 바뀌면 복사된 리스트도 값이 바뀌는 문제 발생!

import copy

x = [15, 64, 7, 3.14, [32, 55], 'ABC']
y = copy.deepcopy(x)
x[0] = 20
x[4][1] = 20
for i in range(len(x)):
    print(f'x[{i}] = {x[i]}, y[{i}] = {y[i]}')

