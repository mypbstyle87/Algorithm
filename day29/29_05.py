# flag OR else
# 문제 설명
# 본 문제에서는 자연수 5개가 주어집니다.
#
# 숫자를 차례로 곱해 나온 수가 제곱수1가 되면 found를 출력하고
# 모든 수를 곱해도 제곱수가 나오지 않았다면 not found를 출력하는
# 코드를 작성해주세요.
#
# 예시 1
# 입력
#
# 2
# 4
# 2
# 5
# 1
# 출력
# found

import math
temp_list = [2, 4, 2, 5, 1]
temp_mul = 1
# for _ in range(5):
#     num = int(input())
#     temp_list.append(num)
for i in range(5):
    temp_mul *= temp_list[i]
    if math.sqrt(temp_mul).is_integer():
        # print(temp_mul)
        print('found')
        break
else:
    print('not found')