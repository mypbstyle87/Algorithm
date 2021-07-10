# 문제
# 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때
# 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면
# 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다.
# 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장
# 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.
#
# 26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다.
# 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다.
# 새로운 수는 26이다.
#
# 위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
#
# N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.
#
# 출력
# 첫째 줄에 N의 사이클 길이를 출력한다.

import sys
import time

num = int(sys.stdin.readline())
# 10 이상이면 나눗셈으로, 1자리 수일경우 10의자리 강제 지정
if num >= 10:
    ten_num = num // 10
    one_num = num % 10
else:
    ten_num = 0
    one_num = num
temp, count, new_num = 0, 0, 0

while (True):
    count += 1
    # 중간 과정 체크
    # print(f'count: {count}')
    # print(ten_num)
    # print(one_num)

    temp = one_num # one_num이 변화하므로 중간 저장
    one_num = (ten_num + one_num) % 10
    ten_num = temp
    # time.sleep(1)

    # 새로 만든 두자리 수가 저장되는 new_num
    new_num = ten_num * 10 + one_num

    # 비교 후 while 탈출 조건 제시
    if new_num == num:
        break

    else:
        ten_num = new_num // 10
        one_num = new_num % 10

print(count)
