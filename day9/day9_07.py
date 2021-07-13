# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
#
# 출력
# 주어진 수들 중 소수의 개수를 출력한다.
#
# 예제 입력
# 4
# 1 3 5 7

import sys

num = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
ans_list = []  # 소수를 연결할 객체
if 1 in num_list:
    num_list.remove(1) # 1은 직접제거
if 2 in num_list:
    ans_list.append(2) # 2는 직접 입력 (단, 이런식으로 직접 제거할경우, 2의 중복이나 1의 중복은 제거 불가)
    num_list.remove(2)
for a in num_list:
    i = 2
    while (True):
        if a % i == 0: # 3 이상 자연수부터 i=2부터 1씩 증가하는 i로 나누어 나누어 떨어지는지 확인
            break
        if i * i > a: # i의 제곱이 a보다 커져버리면, 뒤에는 연산하지 않도록 해서 속도 개선
            ans_list.append(a)
            break
        i += 1
# print(ans_list)
print(len(ans_list))

# 사이에 공백 넣는 출력 방법(리스트 버전)
# count = 0
# for ans in ans_list:
#     count += 1
#     print(ans, end="")
#     if count < len(ans_list):
#         print("", end=" ")
