n = int(input())
stock_list = list(map(int, input().split()))
stock_list.sort()
start = 0
end = len(stock_list) - 1

m = int(input())
order_list = list(map(int, input().split()))
order_list.sort()


def binary_search(array, target, start, end):
    if start > end:
        return None
    middle = (start + end) // 2
    if array[middle] == target:
        return middle
    elif array[middle] > target:
        return binary_search(array, target, start, middle - 1)
    else:
        return binary_search(array, target, middle + 1, end)


for i in order_list:
    if binary_search(stock_list, i, start, end) is None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
