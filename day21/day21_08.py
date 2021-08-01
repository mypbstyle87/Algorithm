# 소수 만들기
# 문제 설명
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때,
# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
# 입출력 예
# nums	result
# [1,2,3,4]	1
# [1,2,7,6,4]	4

def solution(nums):
    from itertools import combinations as cb
    prime_list = [2]
    answer = 0
    # 에라토스테네스의 체
    for i in range(2, 3000):
        j = 2
        while True:
            if i % j == 0:
                break
            else:
                if i <= j * j:
                    prime_list.append(i)
                    break
            j += 1
    nums.sort()

    for i in cb(nums,3):
        comb_sum= sum(i)
        if comb_sum in prime_list:
            answer += 1

    return answer

    # 개선이 필요한 부분 (원래 시간의 6배나 잡아먹게됨)
    # for a in nums:
    #     for b in nums:
    #         if a < b:
    #             for c in nums:
    #                 if b < c and a + b + c in prime_list:
    #                     # print(a, b, c)
    #                     answer += 1


# 타인의 풀이
def solution_other(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer


print(solution([1, 2, 7, 6, 4]))
