# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 A와 B가 주어진다. (0 < A,B < 1010000)
#
# 출력
# 첫째 줄에 A+B를 출력한다.
#
# 예제 입력 1
# 9223372036854775807 9223372036854775808

import sys
a,b = map(int,sys.stdin.readline().split())
print(a+b)
# 파이썬은 큰수의 덧셈도 잘하는구나!