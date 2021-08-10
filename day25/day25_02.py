from typing import Any, MutableSequence


# x = [2, 5, 1, 3, 9, 6, 7, 4]
# print(x)


def reverse_arry(a: MutableSequence) -> None:
    n = len(x)
    for i in range(n // 2):
        x[i], x[n - i - 1] = x[n - i - 1], x[i]


if __name__ == '__main__':
    print('배열의 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요.: '))
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input(f'x[{i}]값을 입력하세요.: '))
    print(x)
    reverse_arry(x)
    print('배열 원소를 역순으로 정렬했습니다.')
    print(x)
