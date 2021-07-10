# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다.
# O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
# 예를 들어, 10번 문제의 점수는 3이 된다.
#
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
#
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다.
# 문자열은 O와 X만으로 이루어져 있다.
#
# 출력
# 각 테스트 케이스마다 점수를 출력한다.
#
# 예제 입력
# 5
# OOXXOXXOOO
# OOXXOOXXOO
# OXOXOXOXOXOXOX
# OOOOOOOOOO
# OOOOXOOOOXOOOOX
import sys

test_num = int(input())
test_line = []

# 리스트에 문자열 입력
for _ in range(test_num):
    string = sys.stdin.readline().rstrip()
    test_line.append(string)

# 잘 입력되었는지 체크
# print(test_line)

# 문자열을 읽고, 문자열의 각 문자를 다시 읽음
for elem in test_line:
    count = 0
    sum = 0
    # 맨 마지막에 O일경우 점수가 누적되지 않는 오류 수정 위해
    letter_last_count = 1
    # 합은 가우스 합계공식 이용
    for letter in elem:
        if letter == "O":
            count += 1
            if letter_last_count==len(elem):
                sum += int(count * (count + 1) / 2)
        else:
            sum += int(count * (count + 1) / 2)
            count = 0
        letter_last_count+=1

    print(sum)
