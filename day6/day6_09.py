# 문제
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
#
# 예를 들어, 서로 다른 9개의 자연수
#
# 3, 29, 38, 12, 57, 74, 40, 85, 61
#
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
#
# 입력
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
#
# 출력
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.
#
# 예제 입력 1
# 3
# 29
# 38
# 12
# 57
# 74
# 40
# 85
# 61


# 최댓값, 최댓값의 위치를 저장할 변수 설정
max_num=0
max_count=0
for i in range(1,10):
    num=int(input())

    # 입력받은 변수와 최댓값이 될 가능성이 있는 값 비교하여 최댓값과 몇번째인지 기록
    if num>max_num:
        max_num=num
        max_count=i
    else:
        pass

print(max_num)
print(max_count)
