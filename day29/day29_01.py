my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])
print(answer)

import itertools
list(itertools.chain(*my_list))

