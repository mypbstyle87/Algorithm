# 피보나치 수 5
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 1 초	256 MB	39862	25214	22118	64.125%
# 문제
# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다.
# 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
#
# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
#
# n=17일때 까지 피보나치 수를 써보면 다음과 같다.
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
#
# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.
#
# 출력
# 첫째 줄에 n번째 피보나치 수를 출력한다.
#
# 예제 입력 1
# 10

# 재귀가 아닌 for문 사용시, 간단함
# fibonaci_list = [0,1]
# for i in range(2, 25):
#     fibonaci_list.append(fibonaci_list[i - 2] + fibonaci_list[i - 1])
# num = int(input())
# print(fibonaci_list[num])


# 재귀로 하면 아주 '논리적'으로 전개 가능^^
def calc_fibonaci(n):
    if n == 0:  # 예외처리 1
        return 0
    if n == 1:  # 예외처리 2
        return 1
    if n >= 2:  # 말 그대로 피보나치를 만들면 된다!
        return calc_fibonaci(n - 1) + calc_fibonaci(n - 2)


num = int(input())
print(calc_fibonaci(num))
