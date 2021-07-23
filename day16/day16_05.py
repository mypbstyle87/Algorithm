# 재도전 필요, 문제를 잘못 읽음

def solution(numbers, hand):
    lhand = [0]
    rhand = [0]
    if hand == "right":
        hand = 'R'
    else:
        hand = 'L'
    print(hand)
    answer = ''
    for i in numbers:
        if i % 3 == 1:
            answer += 'L'
            lhand.append(i//3)
        elif i % 3 == 0 and i != 0:
            answer += 'R'
            rhand.append(i//3-1)
        else:
            if abs(i//3 - lhand[-1]) == abs(rhand[-1] - i//3):
                answer += hand
            elif abs(i//3 - lhand[-1]) > abs(rhand[-1] - i//3):
                answer += 'R'
            else:
                answer += 'L'


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
