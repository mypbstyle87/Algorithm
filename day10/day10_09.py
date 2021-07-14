# 재귀 연습
# 문제
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.
#
# 출력
# 첫째 줄에 N!을 출력한다.
#
# 예제 입력 1
# 10
a = 1


def calc_fact(n):
    if n >= 1:
        return n * calc_fact(n - 1) # 재귀의 경우 리턴에 다음 차수의 식을 써주면 된다.
    else:
        return 1 # 가장 마지막에 연산될 숫자를 적어주면 n*(n-1)... *'1'이 되어 식이 완성되는것.(합의 경우는 return 0)

num=int(input())
print(calc_fact(num))

