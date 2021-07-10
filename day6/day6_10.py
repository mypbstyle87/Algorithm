# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에
# 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
#
# 예를 들어 A = 150, B = 266, C = 427 이라면
# A × B × C = 150 × 266 × 427 = 17037300 이 되고,
# 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.
#
# 입력
# 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다.
# A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.
#
# 출력
# 첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다.
# 마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에
# 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.
#
# 예제 입력 1
# 150
# 266
# 427
# import math

a=int(input())
b=int(input())
c=int(input())
count=1
num=a*b*c
answer=[]
add_num=0
#print(num)
# 자릿수 계산 방법(math 라이브러리 활용)
# while(True):
#     ten_times = int(math.pow(10, count))
#     if num/ten_times<1:
#         break
#     else:
#         count+=1

#print(count)
# 10의 n자리수만큼 연산 수행
while(True):
    # 10으로 나눈 나머지를 계속 배열에 추가하고, 10으로 나눈 몫을 취해서 계속 계산해간다.
    if num==0:
        break
    add_num=num%10
#    print(add_num)
    answer.append(add_num)
    num=num//10



#print(answer)

# 해답 출력 파트
for j in range(0,10):
    print(answer.count(j))