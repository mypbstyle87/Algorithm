# 문제
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
#
# 입력
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.
#
# 출력
# 직사각형의 네 번째 점의 좌표를 출력한다.
#
# 예제 입력
# 5 5
# 5 7
# 7 5

x_cord = [] # x좌표 누적 배열
y_cord = [] # y좌표 누적 배열
for _ in range(3): # 3회 좌표 누적 입력, 배열에 추가
    a, b = map(int, input().split())
    x_cord.append(a)
    y_cord.append(b)

for x in x_cord:
    if x_cord.count(x) == 1: # x좌표 배열에서 1개만 있는 요소의 x좌표가 네번째 점의 x 좌표
        print(x, end=" ")
        break

for y in y_cord:
    if y_cord.count(y) == 1:  # y좌표 배열에서 1개만 있는 요소의 y좌표가 네번째 점의 y 좌표
        print(y, end="")
        break
