# https://programmers.co.kr/learn/courses/30/lessons/42840
# 모의고사
# 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다.
# 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
# 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.
#
# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
#
# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.
#
# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
# 입출력 예
# answers	return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2] [1,2,3]

def solution(answers):
    count1, count2, count3 = 0, 0, 0
    temp1 = [2, 1, 2, 3, 2, 4, 2, 5]
    temp2 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []
    # 정답 비교 후 각 count에 누적
    for i in range(1, len(answers) + 1):
        # 그냥 가독성을 위해서 temp1, temp2, temp3에 패턴을 전부 저장할껄
        if (i % 5 if i % 5 else 5) == answers[i - 1]: # 괜히 컴프리헨션 사용해보겠다고 복잡하게 만든듯..
            count1 += 1
        if temp1[i % 8 - 1] == answers[i - 1]:
            count2 += 1
        if temp2[i % 10 - 1] == answers[i - 1]:
            count3 += 1
    temp3 = [count1, count2, count3]
    return [j+1 for j in range(3) if max(temp3)==temp3[j]]


print(solution([1, 2, 3, 4, 5, 4, 3, 2, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
