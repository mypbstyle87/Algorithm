# 나누어 떨어지는 숫자 배열
# 문제 설명
# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
#
# 제한사항
# arr은 자연수를 담은 배열입니다.
# 정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
# divisor는 자연수입니다.
# array는 길이 1 이상인 배열입니다.
# 입출력 예
# arr	divisor	return
# [5, 9, 7, 10]	5	[5, 10]

def solution(arr, divisor):
    temp_list = [i for i in arr if i % divisor == 0]
    temp_list.sort()
    return temp_list if len(temp_list) else [-1]


# 타인의 풀이, or 사용에 주목
def solution_other(arr, divisor):
    return sorted([n for n in arr if n % divisor == 0]) or [-1]
