# 문제
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이
# 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
#
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다.
# 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.
#
# 출력
# 첫째 줄에 그룹 단어의 개수를 출력한다.
#
# 예제 입력
# 3
# happy
# new
# year
import sys

num = int(input())
strings = [] # 입력받은 문자열들을 연결할 배열
ans_list = [] # 각 문자열의 문자를 쪼개서 연결할 배열
sum = 0 # 그룹 단어 누적 변수

for _ in range(num):
    strings.append(sys.stdin.readline().strip())

for string in strings:
    # print(string)
    for letter in string: # 각 문자열의 단어별로
        # print(letter)
        if letter not in ans_list or letter == ans_list[-1]: # 문자가 ans_list에 아예 없거나, 배열의 마지막 문자와 같다면 ans_list에 추가
            ans_list.append(letter)
    # print(ans_list)
    if len(ans_list) == len(string): # 만약 그룹단어라면, ans_list의 원소 갯수와, 문자열의 길이가 같아야한다.
        sum += 1
    ans_list.clear() # ans_list 초기화
print(sum)
