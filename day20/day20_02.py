# 두 개 뽑아서 더하기
# 문제 설명
# 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아
# 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# numbers의 길이는 2 이상 100 이하입니다.
# numbers의 모든 수는 0 이상 100 이하입니다.
# 입출력 예
# numbers	result
# [2,1,3,4,1]	[2,3,4,5,6,7]
# [5,0,2,7]	[2,5,7,9,12]

def solution(numbers):
    answer = []
    for i1, n in enumerate(numbers):
        for i2, j in enumerate(numbers):
            if i1 != i2 :
                answer.append(n+j)

    set_answer = set(answer)
    return sorted(list(set_answer))