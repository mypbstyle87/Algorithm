# 문제
# 셀프 넘버는 1949년 인도 수학자 D.R. Kaprekar가 이름 붙였다.
# 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자.
# 예를 들어, d(75) = 75+7+5 = 87이다.
#
# 양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다.
#
# 예를 들어, 33으로 시작한다면 다음 수는 33 + 3 + 3 = 39이고,
# 그 다음 수는 39 + 3 + 9 = 51, 다음 수는 51 + 5 + 1 = 57이다.
# 이런식으로 다음과 같은 수열을 만들 수 있다.
#
# 33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...
#
# n을 d(n)의 생성자라고 한다. 위의 수열에서 33은 39의 생성자이고,
# 39는 51의 생성자, 51은 57의 생성자이다. 생성자가 한 개보다 많은 경우도 있다.
# 예를 들어, 101은 생성자가 2개(91과 100) 있다.
#
# 생성자가 없는 숫자를 셀프 넘버라고 한다. 100보다 작은 셀프 넘버는 총 13개가 있다.
# 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97
#
# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
#
# 입력
# 입력은 없다.
#
# 출력
# 10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.

# 가장 깔끔하게 자리수 합을 만들어 낸 함수같다.
def producter(a):
    num = a
    sum = a % 10
    while (a // 10 >= 1):
        a = a // 10
        sum += a % 10
    sum += num
    return sum

# 1~ 10000까지 들어있는 배열
num_list = []
garbage_list = []
for i in range(1, 10001):
    num_list.append(i)

# 시간복잡도가 너무 높아서 개선 필요.
for j in num_list:
    while (True):
        if producter(j) in garbage_list or producter(j) > 10000:
            break
        else:
            garbage_list.append(producter(j))
            j = producter(j)

            # 시간복잡도를 급격하게 높히는 부분!
            # else:
            #     if producter(j) in num_list:
            #         num_list.remove(producter(j))
            #     j = producter(j)

for k in num_list:
    if k not in garbage_list:
        print(k)




