# 실패율
# 문제 설명
#
# 슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌다. 그녀가 만든 프랜즈 오천성이 대성공을 거뒀지만, 요즘 신규 사용자의 수가 급감한 것이다.
# 원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였다.
#
# 이 문제를 어떻게 할까 고민 한 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했다. 역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만,
# 실패율을 구하는 부분에서 위기에 빠지고 말았다. 오렐리를 위해 실패율을 구하는 코드를 완성하라.
#
# 실패율은 다음과 같이 정의한다.
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때,
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.
#
# 제한사항
# 스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
# stages의 길이는 1 이상 200,000 이하이다.
# stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
# 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
# 단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
# 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
# 입출력 예
# N	stages	result
# 5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
# 4	[4,4,4,4,4]	[4,1,2,3]
# 입출력 예 설명
# 입출력 예 #1
# 1번 스테이지에는 총 8명의 사용자가 도전했으며, 이 중 1명의 사용자가 아직 클리어하지 못했다. 따라서 1번 스테이지의 실패율은 다음과 같다.
#
# 1 번 스테이지 실패율 : 1/8
# 2번 스테이지에는 총 7명의 사용자가 도전했으며, 이 중 3명의 사용자가 아직 클리어하지 못했다. 따라서 2번 스테이지의 실패율은 다음과 같다.
#
# 2 번 스테이지 실패율 : 3/7
# 마찬가지로 나머지 스테이지의 실패율은 다음과 같다.
#
# 3 번 스테이지 실패율 : 2/4
# 4번 스테이지 실패율 : 1/2
# 5번 스테이지 실패율 : 0/1
# 각 스테이지의 번호를 실패율의 내림차순으로 정렬하면 다음과 같다.
#
# [3,4,2,1,5]


def solution(N, stages):
    import operator
    ratio_dict = {}
    user_num = len(stages)
    for stage_num in range(1, N + 1):
        if user_num:
            ratio_dict[stage_num] = stages.count(stage_num) / user_num
        else:
            ratio_dict[stage_num] = 0
        user_num -= stages.count(stage_num)
    ratio_dict = sorted(ratio_dict.items(), key=operator.itemgetter(1), reverse=True)
    return [i[0] for i in ratio_dict]

# 타인의 풀이
# result는 dictionary이므로 sorted에 result를 그냥 넘기면 result의 keys가 들어갑니다.
# keys는 생략이 가능합니다. 거기에 lambda는 기준을 result[x]: 즉 value로 정렬한다는 뜻입니다. 그래서 key가 출력되게 됩니다.
# 매번 count 하지 않고 초반에 사전으로 미리 각 스테이지별 인원을 집계해두면 정렬을 제외 했을 때 O(n)의 시간복잡도로 풀 수 있습니다.
def solution_other(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)



print(solution(4, [2,2,2,2,2]))
