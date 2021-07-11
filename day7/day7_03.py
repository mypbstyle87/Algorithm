# 문제
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
#
# 출력
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

def calc_hansu(a):
    if a < 100:
        print(a)
    else:
        sum = 99
        for i in range(100, a + 1):
            # 각각의 자리수를 저장하는 변수 설정
            one_num = i % 10
            ten_num = i // 10 % 10
            hun_num = i // 10 // 10

            # 등차수열의 가운데항 * 2 = 전항 + 후항
            if ten_num * 2 == (one_num + hun_num):
                sum += 1

        print(sum)

num = int(input())
calc_hansu(num)
