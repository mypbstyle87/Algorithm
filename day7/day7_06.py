# 문제
# 알파벳 소문자로만 이루어진 단어 S가 주어진다.
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며,
# 알파벳 소문자로만 이루어져 있다.
#
# 출력
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치,
# ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
#
# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다.
# 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.
#
# 예제 입력
# baekjoon
# 예제 출력
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1


s = input()
ans_list = []
# 처리하기 쉽게 1차원 배열로 정의
for letter in s:
    ans_list.append(letter)
# print(ans_list)


for i in 'abcdefghijklmnopqrstuvwxyz':
    # ans_list의 모든 문자에 대해서 연산 수행
    if i not in ans_list:  # in이라서 개선 필요
        print("-1", end="")
    else:
        print(ans_list.index(i), end="")  # index가 참 요긴하게 쓰였다.

    # 끝이 어딘지 알기 때문에 마지막 space 제거가 용이했다.
    if i != 'z':
        print(" ", end="")

    # index 모를때 enumerate로 구현한것. 단 마지막 space가 제거가 안된 상태이다.
    # for k,v in enumerate(ans_list):
    #     if i not in ans_list:
    #         print("-1", end="")
    #         break
    #     elif v==i:
    #         print(f'{k}', end="")
    #         break
