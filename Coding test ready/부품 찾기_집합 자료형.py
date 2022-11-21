n = int(input())
stock_list = set(map(int, input().split()))

m = int(input())
order_list = list(map(int, input().split()))
order_list.sort()

for i in order_list:
    if i in stock_list:
        print('yes', end=' ')
    else:
        print('no', end=' ')