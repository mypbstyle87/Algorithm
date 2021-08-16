# 2차원 리스트 뒤집기
# 문제 설명
# 다음을 만족하는 함수, solution을 완성해주세요.
#
# solution 함수는 이차원 리스트, mylist를 인자로 받습니다
# solution 함수는 mylist 원소의 행과 열을 뒤집은 한 값을 리턴해야합니다.
# 예를 들어 mylist [[1, 2, 3], [4, 5, 6], [7, 8, 9]]가 주어진 경우, solution 함수는 [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 을 리턴하면 됩니다.
#
# 제한 조건
# mylist의 원소의 길이는 모두 같습니다.
# mylist의 길이는 mylist[0]의 길이와 같습니다.
# 각 리스트의 길이는 100 이하인 자연수입니다.
import copy

mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
temp_list = []
ans_list = []
size = len(mylist)
for i in range(size):
    for j in mylist:
        temp_list.append(j[i])
    ans_list.append(temp_list)
    ans_list = copy.deepcopy(ans_list)
    print(temp_list)
    temp_list.clear()
print(ans_list)
