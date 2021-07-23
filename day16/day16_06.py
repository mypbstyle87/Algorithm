# 정수 내림차순으로 배치하기
# 문제 설명
# 함수 solution은 정수 n을 매개변수로 입력받습니다.
# n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
# 예를들어 n이 118372면 873211을 리턴하면 됩니다.
#
# 제한 조건
# n은 1이상 8000000000 이하인 자연수입니다.
# 입출력 예
# n	     return
# 118372 873211

# 나의 풀이
def solution(n):
    temp_list = []
    answer = ''
    for num in str(n):
        temp_list.append(int(num)) # 일시적으로 각각의 숫자를 저장할 리스트에 각 숫자 추가
    temp_list.sort(reverse=True) # 리스트 역순 정렬
    for num_2 in temp_list:
        answer += str(num_2) # 리스트의 숫자를 문자 형태로 answer에 추가
    return int(answer) # 정수로 반환

# 타인의 풀이
def solution_other(n):
    return int("".join(sorted(str(n),reverse = True)))

print(solution_other(118372))
