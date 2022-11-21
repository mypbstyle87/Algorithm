def binary_search(array, target, start, end):
    # 예외처리
    if start > end:
        return None
    # 중간 인덱스 계산
    middle = (start + end) // 2
    # 중간 인덱스와 target의 관계에 따라 인덱스 반환, 또는 재귀
    if array[middle] == target:
        return middle
    elif array[middle] < target:
        return binary_search(array, target, middle + 1, end)  # 재귀는 return f(X)꼴 임을 명신
    else:
        return binary_search(array, target, start, middle - 1)


n, targ = map(int, input().split())
arr = list(map(int, input().split()))
st = 0
en = n - 1

result = binary_search(arr, targ, st, en)
if result is None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
