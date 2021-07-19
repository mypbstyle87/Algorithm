# 최대공약수와 최소공배수
# 문제 설명
# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
# 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
# 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.
#
# 제한 사항
# 두 수는 1이상 1000000이하의 자연수입니다.
# 입출력 예
# n	m	return
# 3	12	[3, 12]
# 2	5	[1, 10]

def solution(n, m):
    answer = []
    for i in range(min(n, m) + 1, 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            answer.append(n * m // i)  # 최대공약수 * 최소공배수 = 두수의 곱으로 계산하면 최대공약수는 따로 계산 불필요
            break
    return answer
    # 최소공배수 구하는 방법(굉장히 오래걸릴듯 ㅋㅋ..)
    #    for j in range(max(n, m), n * m + 1):
    #         if j % n == 0 and j % m == 0:
    #             answer.append(j)
    #             break


# 다른사람 코드(유클리드 호제법+재귀문)
def Euclidean(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return Euclidean(b, r)

print(Euclidean(25,10))