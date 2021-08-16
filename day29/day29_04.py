# 가장 많이 등장하는 알파벳 찾기
# 문제 설명
# 이 문제에는 표준 입력으로 문자열, mystr이 주어집니다. mystr에서 가장 많이 등장하는 알파벳만을 사전 순으로 출력하는 코드를 작성해주세요.
#
# 제한 조건
# mystr의 원소는 알파벳 소문자로만 주어집니다.
# mystr의 길이는 1 이상 100 이하입니다.
# 예시
# input	output
# 'aab'	'a'
# 'dfdefdgf'	'df'
# 'bbaa'

import string
import operator
my_str = input().strip()
answer_dict = {}
answer = ''
for i in string.ascii_lowercase:
    answer_dict[i] = my_str.count(i)

s_dict = sorted(answer_dict.items(), key = operator.itemgetter(1), reverse=True)
max = s_dict[0][1]
for i in s_dict:
    if i[1] != max:
        break
    answer += i[0]

print(answer)