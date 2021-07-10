# 문제
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다.
# 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
#
# 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다.
# 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
#
# 출력
# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다.
# X보다 작은 수는 적어도 하나 존재한다.

# 마지막 문자를 출력할떄 공백처리때문에, 코드가 지저분해졌다.
# 분명 깔끔하게 처리할 수 있는 방법이 있을텐데..

import sys

num, comp_num = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
space_count = 0
max_count = 0
# 공백처리를 위해 전체 리스트를 두번 검산하게된다.(개선필요)
for j in num_list:
    if j < comp_num:
        max_count += 1
# print(f'갯수: {max_count}')
for i in num_list:

    # 문제의 공백처리부분
    if i < comp_num:
        if space_count != max_count - 1:
            space_count += 1
            print(f'{i} ', end="")
        else:
            print(f'{i}', end="")

    else:
        pass
