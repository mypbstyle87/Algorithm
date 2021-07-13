# 문제
# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
#
# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97
# 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.
#
# 입력
# 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
#
# M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.
#
# 출력
# M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다.
#
# 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.
#
# 예제 입력
# 60
# 100

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


num1 = int(input())
num2 = int(input())

ans_list_num = calc_num(num1, num2)  # 소수를 연결할 객체

if ans_list_num:
    print(sum(ans_list_num)) # 리스트의 소수 합계
    print(ans_list_num[0]) # 최솟값(리스트의 첫번째 값 출력)
else:
    print(-1) # 예외처리
