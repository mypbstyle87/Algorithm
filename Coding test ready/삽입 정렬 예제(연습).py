array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def insert_sort(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break # 삽입정렬은 앞에는 다 정렬이 되어 있으니깐..

insert_sort(array)
print(array)