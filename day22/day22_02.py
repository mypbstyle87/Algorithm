# 소수 찾기
# 문제 설명
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
#
# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)
#
# 제한 조건
# n은 2이상 1000000이하의 자연수입니다.
# 입출력 예
# n	result
# 10	4
# 5	3
# 입출력 예 설명
# 입출력 예 #1
# 1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환
#
# 입출력 예 #2
# 1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환

def solution(n):
    temp_list = [2]
    count = 0
    for i in range(3, 1000001):
        for j in range(2, i):
            if i % j == 0:
                break
            if j * j > i:
                temp_list.append(i)
                break
    print(temp_list)
    for k in temp_list:
        if k <= n:
            count += 1
        if k > n:
            break
    return count


def prime_list(n):  # n 까지의 소수 list 반환하는 에라토스 테네스의 체
    # 에라토스테네스의 체 초기화: n + 1개 요소에 True 설정(소수로 간주)
    sieve = [True] * (n + 1) # n+1번째 요소가 인덱스 기준으로 'n'번째임

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:  # i가 소수인 경우
            for j in range(i + i, n + 1, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n + 1) if sieve[i] == True]

# 타인의 답

def solution_other(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)


print(prime_list(14))
