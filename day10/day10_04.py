# 문제
# 한수는 지금 (x, y)에 있다. 직사각형의 왼쪽 아래 꼭짓점은 (0, 0)에 있고,
# 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 x, y, w, h가 주어진다.
#
# 출력
# 첫째 줄에 문제의 정답을 출력한다.
#
# 제한
# 1 ≤ w, h ≤ 1,000
# 1 ≤ x ≤ w-1
# 1 ≤ y ≤ h-1
# x, y, w, h는 정수
# 예제 입력 1
# 6 2 10 3

import sys

cordinates = list(map(int, sys.stdin.readline().split()))

x_dif_1 = cordinates[0] # 0 과 해당 점의 x좌표간 거리
x_dif_2 = cordinates[2] - cordinates[0] # 직사각형의 오른쪽 끝에서 해당 점까지의 거리
y_dif_1 = cordinates[1] # 0과 해당 점의 y좌표간 거리
y_dif_2 = cordinates[3] - cordinates[1] # 직사각형의 위에서 해당 점까지의 거리

ans_list = [x_dif_1, x_dif_2, y_dif_1, y_dif_2] # 최소값 구하기 위해 모두 리스트에 입력
print(min(ans_list)) # 최소값 출력
