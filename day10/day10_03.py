# 문제
#
# 골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다.
# 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다.
# 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다.
# 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
#
# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오.
# 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.
#
# 출력
# 각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.
#
# 제한
# 4 ≤ n ≤ 10,000
# 예제 입력
# 3
# 8
# 10
# 16

# 에라토스테네스 체로 소수 리스트 구현, 2는 소수이므로 먼저 집어넣어줌.
prime_list = [2]
for i in range(3, 10000):  # 10000까지 소수 리스트 작성
    div = 2
    while True:
        if i % div != 0:  # 계속 써먹고 있는 소수 계산방법
            if div * div > i:
                # print(i)
                prime_list.append(i)
                break
        else:
            break
        div += 1

test_num = int(input())
for _ in range(test_num):
    num = int(input())
    for j in range(num // 2, 1, -1): # 입력받은 숫자값의 절반부터 시작해서, 역순으로 검색(그래야 차이가 최소), end number는 '1' 이어야 소수 2까지 포함됨
        if j in prime_list and (num - j) in prime_list: # 어떤 소수와 입력값 - 소수가 둘다 소수 리스트에 있으면 골드바흐 파티션
            print(j, num - j)
            break # 1개 출력후 추가 출력 막기 위해 break
