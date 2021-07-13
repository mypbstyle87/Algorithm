# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다.
# (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
#
# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
#
# 예제 입력
# 3 16

def calc_num(num_1, num_2):  # 주어진 두 수 사이에서 존재하는 소수를 계산하는 함수 설정
    ans_list = []
    if num_1 <= 2 and num_2 >= 2:  # 2 별도 처리(2는 여기에 있어야 리스트에서 0번으로 저장됨)
        ans_list.append(2)
    for a in range(num_1, num_2 + 1):
        i = 2
        while (True):
            if a % i == 0:  # 3 이상 자연수부터 i=2부터 1씩 증가하는 i로 나누어 나누어 떨어지는지 확인
                break
            if i * i > a:  # i의 제곱이 a보다 커져버리면, 뒤에는 연산하지 않도록 해서 속도 개선
                ans_list.append(a)
                break
            i += 1
    if 1 in ans_list:
        ans_list.remove(1)
    return ans_list

import sys
num1,num2=map(int,sys.stdin.readline().split())

ans_list_num = calc_num(num1, num2)  # 소수를 연결할 객체

for ans in ans_list_num: # 리스트 내의 소수 출력
    print(ans)
