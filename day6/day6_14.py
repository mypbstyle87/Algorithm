# 문제
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
#
# 입력
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
#
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
# 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
#
# 출력
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
#
# 예제 입력
# 5
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91
import sys

test_num = int(input())
for _ in range(test_num):

    test_data_list = list(map(int, sys.stdin.readline().split()))
    student_num = test_data_list.pop(0)
    # print(student_num)
    # print(test_data_list)
    average = (sum(test_data_list)) / student_num

    # 평균을 초과하는 학생 수를 count에 저장
    count = 0

    for score in test_data_list:
        if score > average:
            count += 1
        else:
            pass
    # 평균 초과 학생 비율 계산
    ratio = count / student_num * 100
    # format 함수 쓰는법 : format(변수, "형식")
    print(format(ratio, ".3f") + "%")
