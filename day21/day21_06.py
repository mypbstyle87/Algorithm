# 스킬트리
# 문제 설명
# 선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 뜻합니다.
#
# 예를 들어 선행 스킬 순서가 스파크 → 라이트닝 볼트 → 썬더일때, 썬더를 배우려면 먼저 라이트닝 볼트를 배워야 하고, 라이트닝 볼트를 배우려면 먼저 스파크를 배워야 합니다.
#
# 위 순서에 없는 다른 스킬(힐링 등)은 순서에 상관없이 배울 수 있습니다. 따라서 스파크 → 힐링 → 라이트닝 볼트 → 썬더와 같은 스킬트리는 가능하지만,
# 썬더 → 스파크나 라이트닝 볼트 → 스파크 → 힐링 → 썬더와 같은 스킬트리는 불가능합니다.
#
# 선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질 때, 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.
#
# 제한 조건
# 스킬은 알파벳 대문자로 표기하며, 모든 문자열은 알파벳 대문자로만 이루어져 있습니다.
# 스킬 순서와 스킬트리는 문자열로 표기합니다.
# 예를 들어, C → B → D 라면 "CBD"로 표기합니다
# 선행 스킬 순서 skill의 길이는 1 이상 26 이하이며, 스킬은 중복해 주어지지 않습니다.
# skill_trees는 길이 1 이상 20 이하인 배열입니다.
# skill_trees의 원소는 스킬을 나타내는 문자열입니다.
# skill_trees의 원소는 길이가 2 이상 26 이하인 문자열이며, 스킬이 중복해 주어지지 않습니다.
# 입출력 예
# skill	skill_trees	return
# "CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2

def solution(skill, skill_trees):
    temp_answer = ""
    answer = 0
    for temp in skill_trees: # skill tree 내부의 요소에서 skill에 없는 요소들을 제거하여 temp_answer라는 새로운 문자열 생성
        for temp_order in temp:
            if temp_order in skill:
                temp_answer += temp_order
            else:
                pass
        print(temp_answer)
        for k, i in enumerate(temp_answer): # temp_answer에서 skill tree 순서와 맞지 않는 부분이 있다면 answer에서 1 차감
            if skill[k] != i:
                answer -= 1
                break
        answer += 1 # 만약 skill tree로 형성 가능하였다면 +1이고 아니라면 -1 +1이어서 결국 0
        temp_answer = ""
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
