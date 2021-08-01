# day21_04 코드 효율화

def solution(n):
    import math
    def calc_3(k):
        count = 0
        answer = 0
        # 재귀로 할수 없는 상황! 04가 최적화 버전임!
        # temp_str = calc_3(k // 3) + str(k % 3) if k >= 3 else str(k % 3)
        # for num in temp_str:
        #     answer += int(num) * math.pow(3, count)
        #     count += 1
        # return int(answer)
    return calc_3(n)

print(solution(45))