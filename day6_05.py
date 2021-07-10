# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
#
# 각 테스트 케이스는 한 줄로 이루어져 있으며,
# 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#
# 입력이 없으면 종료한다.
#
# 출력
# 각 테스트 케이스마다 A+B를 출력한다.

import sys

while (True):
    c = sys.stdin.readline().split()
    if len(c) == 0:
        break
    else:
        a = int(c[0])
        b = int(c[1])
        print(a + b)
