# 문제
# 과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다.
# 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
#
# 입력
# 입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다.
# 각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.
#
# 출력
# 각 입력에 대해 직각 삼각형이 맞다면 "right", 아니라면 "wrong"을 출력한다.
#
# 예제 입력
# 6 8 10
# 25 52 60
# 5 12 13
# 0 0 0
import sys
def calc_pita(a,b,c): # 피타고라스 계산 함수
    if c > b and c > a: # c가 빗변이면
        if c * c == b * b + a * a: # c로 구한 피타고라스 정리가 맞아야함.
            print('right')
        else: # c가 가장 긴변인데 피타가 안맞으면 wrong
            print('wrong')
    elif b > a and b > c:
        if b * b == a * a + c * c:
            print('right')
        else:
            print('wrong')
    elif a > b and a > c:
        if a * a == b * b + c * c:
            print('right')
        else:
            print('wrong')
    else: # 어떤 변도 가장 긴 변이 없다면, 빗변이 될 수 있는 변이 없다.
        print('wrong')

while True:
    num1,num2,num3= map(int,sys.stdin.readline().split())
    if num1==0 and num2==0 and num3==0: # 예외 처리
        break
    calc_pita(num1,num2,num3) # 함수 호출


