# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
#
# 출력
# 1부터 n까지 합을 출력한다.

# gauss way
# num=int(input())
# sum=int((num+1)*num/2)
# print(sum)

# for문 사용
num=int(input())
sum=0

for i in range(1,num+1):
    sum+=i

print(sum)