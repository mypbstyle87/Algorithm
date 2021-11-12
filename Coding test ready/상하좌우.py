from typing import List, Tuple

mat_num = int(input())
move_str = input().split()


def where_am_i(arr: List) -> Tuple:
    r_count = 1
    d_count = 1
    for i in arr:
        if i == 'R' and r_count <= mat_num - 1:
            r_count += 1
        elif i == 'D' and d_count <= mat_num - 1:
            d_count += 1
        elif i == 'L' and r_count >= 2:
            r_count -= 1
        elif i == 'U' and d_count >= 2:
            d_count -= 1
    return d_count, r_count


print(*where_am_i(move_str))
