# 문제
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
#
# 출력
# 입력으로 주어진 숫자 N개의 합을 출력한다.
#
# 예제 입력
# 1
# 1
import sys

# 자료 입력받기
test_case_num = int(input())
data_list = list(sys.stdin.readline().split())
# 누적 합 저장 변수
sum = 0
# 리스트의 첫번째 배열의 각 문자를 읽는다.
for letter in data_list[0]:
    # print(int(letter))
    sum += int(letter)
print(sum)
