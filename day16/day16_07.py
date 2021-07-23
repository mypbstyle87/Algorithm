# 자연수 뒤집어 배열로 만들기
# 문제 설명
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.
# 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
#
# 제한 조건
# n은 10,000,000,000이하인 자연수입니다.
# 입출력 예
# n	return
# 12345	[5,4,3,2,1]

# 나의 풀이
def solution(n):
    answer = []
    for i in str(n):
        answer.insert(0, int(i)) # 0번 인덱스에 정수로 casting한 원소를 계속 삽입
    return answer


# 타인의 풀이
def digit_reverse(n):
    return [int(i) for i in str(n)][::-1]

print(solution(12345))
