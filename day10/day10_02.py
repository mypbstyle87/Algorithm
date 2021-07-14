# day10_01의 시간초과 문제로, 에라토스테네스의 체를 먼저 구현, 갯수를 구하는 형식으로 발전
# 확실히 모든 입력값에 대해서 처음부터 소수를 계산하는건 극도록 비효율. 입력값의 범위를 알때는 체를 먼저 구현하는것이 합리적


# 에라토스테네스 체로 소수 리스트 구현, 2는 소수이므로 먼저 집어넣어줌.
prime_list=[2]
for i in range(3,246920):
    div=2
    while True:
        if i%div!=0: # 계속 써먹고 있는 소수 계산방법
            if div*div>i:
                # print(i)
                prime_list.append(i)
                break
        else:
            break
        div+=1

while True:
    count=0
    num=int(input())
    if num==0: # 예외처리
        break
    for j in prime_list: # 소수 갯수에 대해서
        if num<j and j<2*num+1:
            count+=1
        if j>=2*num+1: # j가 2n+1 이상이 되면 for문 종료(속도개선)
            break
    print(count)