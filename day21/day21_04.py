# 3진법 뒤집기
# 문제 설명
# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# n은 1 이상 100,000,000 이하인 자연수입니다.
# 입출력 예
# n	result
# 45	7
# 125	229

def solution(n):
    import math
    def calc_3(k):
        return calc_3(k // 3) + str(k % 3) if k >= 3 else str(k % 3)

    def calc_10(l):
        count = 0
        answer = 0
        for num in l[::-1]: # 역순으로 3의 자승을 곱해감
            answer += int(num) * math.pow(3, count)
            count += 1
        return int(answer)

    temp_str = calc_3(n)[::-1] # revese된 3진수 표기
    return calc_10(temp_str)

print(solution(3))