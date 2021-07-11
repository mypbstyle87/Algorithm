# 알파벳 대소문자로 된 단어가 주어지면,
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.
#
# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
# 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
#
# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
#
# 예제 입력
# Mississipii

import sys

string = sys.stdin.readline().rstrip()
string = string.upper() # 대문자로 변경하여 비교하기
ans_dict = {} # 문자별로 갯수 세기
switch_dict = {} # k, v -> v, k로 변경하여 가장 갯수 많은 문자 출력에 이용
# print(string)
# ans_dict에 갯수 누적
for letter in string:
    if letter not in ans_dict:
        ans_dict[letter] = 1
    else:
        ans_dict[letter] += 1
# switch_dict에 v, k 꼴 딕셔너리 입력
for k, v in ans_dict.items():
    switch_dict[v] = k

# count 사용하기 위해서 list로 변경
ans_list = list(ans_dict.values())
# 최대 갯수 몇개인지 확정
max = max(ans_dict.values())


if ans_list.count(max) > 1: # max count가 2개 이상이면 ? 출력
    print("?")
else:
    print(switch_dict[max]) # 아니면 최대 갯수를 갖고 있는 k를 출력
