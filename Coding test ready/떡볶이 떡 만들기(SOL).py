n, m = map(int, input().split())
length_list = list(map(int, input().split()))

start = 0
end = max(length_list)

# 이진 탐색 수행(반복적)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in length_list:
        if i > mid:
            total += i - mid
    if total == m:
        result = mid
        break
    elif total > m:
        result = mid # 이부분이 포인트(적어도 떡을 필요한 만큼은 가져갈 수 있도록 이쪽에 result를 걸어놓아야함)
        start = mid + 1
    else:
        end = mid - 1

print(result)