n = int(input())
stock_list = list(map(int, input().split()))
stock_list_sorted = [0] * (max(stock_list) + 1)
for i in stock_list:
    stock_list_sorted[i] += 1


m = int(input())
order_list = list(map(int, input().split()))

for i in order_list:
    if stock_list_sorted[i] >= 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')