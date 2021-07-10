# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
#
# 각 테스트 케이스는 한 줄로 이루어져 있으며,
# 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#
# 출력
# 각 테스트 케이스마다 A+B를 출력한다.

# input으로 자료를 100000번 받으면 시간 초과가 발생한다.
# 이경우 sys.stdin.readline()으로 읽어줘야한다.[빠른 입출력]
# 줄단위로 읽으면 개행 문자를 같이 받으므로, 개행문자(\n)제거 필요.
# str 타입으로 저장되므로, 정수로 사용하기 위한 형변환이 필요.

import sys
num_testTimes=int(input())
for i in range(num_testTimes):
    a,b=map(int,sys.stdin.readline().split())
    print(a+b)
