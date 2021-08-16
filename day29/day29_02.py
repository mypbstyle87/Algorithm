# 순열과 조합
# 문제 설명
# 숫자를 담은 일차원 리스트, mylist에 대해 mylist의 원소로 이루어진 모든 순열을 사전순으로 리턴하는 함수 solution을 완성해주세요.
#
# 제한 조건
# mylist 의 길이는 1 이상 100 이하인 자연수입니다.
# 예시
# mylist	output
# [2, 1]	[[1, 2], [2, 1]]
# [1, 2, 3]	[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

a=[2,1,3]

def solution(mylist):
    import itertools
    ans = sorted(map(list, itertools.permutations(mylist)))
    return ans

print(solution(a))


pool = ['C', 'B', 'A']
def sol_others(pool):
    import itertools
    print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
    print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기

sol_others(pool)