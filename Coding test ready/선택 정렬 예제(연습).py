array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def choice_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

choice_sort(array)
print(array)