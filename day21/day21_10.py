def solution(numbers, hand):
    import re
    lhand_row = 3
    lhand_column = 0

    rhand_row = 3
    rhand_column = 2

    answer = ''
    # [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"

    # 0 1 2
    # 3 4 5
    # 6 7 8
    # * 9 # 로 바꿔서 위치 받음(row = 위부터 0, column = 왼쪽부터 0)

    for i in numbers:
        if str(i) in "147":
            answer += 'L'
            lhand_row = (i - 1) // 3
            lhand_column = (i - 1) % 3
        elif str(i) in "369":
            answer += 'R'
            rhand_row = (i - 1) // 3
            rhand_column = (i - 1) % 3
        else:
            if i == 0:
                row = 3
                column = 1
            elif str(i) in "258":
                row = (i - 1) // 3
                column = (i - 1) % 3

            l_distance = abs(lhand_row - row) + abs(lhand_column - column)
            r_distance = abs(rhand_row - row) + abs(rhand_column - column)
            print("왼쪽거리",l_distance)
            print("오른쪽거리",r_distance)

            if l_distance < r_distance:
                answer += 'L'
                lhand_row = row
                lhand_column = column
            elif r_distance < l_distance:
                answer += 'R'
                rhand_row = row
                rhand_column = column
            else:
                if hand == 'right':
                    answer += 'R'
                    rhand_row = row
                    rhand_column = column
                else:
                    answer += 'L'
                    lhand_row = row
                    lhand_column = column

    return answer

# 타인의 풀이(딕셔너리)
def solution_other(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))


