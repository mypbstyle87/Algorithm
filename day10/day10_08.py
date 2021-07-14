# 문제
#
# 이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다.
# 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.
#
# 조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고,
# 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때,
# 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 이루어져 있다.
#
# 한 줄에 x1, y1, r1, x2, y2, r2가 주어진다. x1, y1, x2, y2는 -10,000보다 크거나 같고,
# 10,000보다 작거나 같은 정수이고, r1, r2는 10,000보다 작거나 같은 자연수이다.
#
# 출력
# 각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다. 만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.
#
# 예제 입력
# 3
# 0 0 13 40 0 37
# 0 0 3 0 7 4
# 1 1 1 1 1 5

# 출력
# 2
# 1
# 0

import sys
import math

test_num = int(input())
for _ in range(test_num):
    data = list(map(int, sys.stdin.readline().split())) # list에 좌표값들 저장
    # 원의 중심간 거리 d 계산
    distant_centers = math.sqrt((data[0] - data[3]) * (data[0] - data[3]) + (data[1] - data[4]) * (data[1] - data[4]))
    # 반지름의 합계 s 계산
    sum_radius = data[2] + data[5]
    # 반지름의 차이의 절댓값 l 계산
    subtract_radius = abs(data[2] - data[5])

    # 만약 완전히 같은 원이면 -1 출력
    if data[0] == data[3] and data[1] == data[4] and data[2] == data[5]:
        print(-1)
    else:
        if sum_radius < distant_centers: # s < d이면 원은 만날수 없음 : 0개 교점
            print(0)
        elif sum_radius == distant_centers: # s == d 이면 원은 접함 : 1개 교점
            print(1)
        elif sum_radius > distant_centers: # s > d 인경우,
            if subtract_radius == distant_centers: # l == d 인경우 안쪽에서 두 원이 접함 : 1개 교점
                print(1)
            elif subtract_radius > distant_centers: # l > d 인경우 한 원 내부에 다른 원이 만나지 않고 존재 : 0개 교점
                print(0)
            else:
                print(2) # 이경우를 제외하면 두 원은 2번 만남 : 2개 교점
