array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort_py(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]

    arr_left = [x for x in tail if x <= pivot]
    arr_right = [x for x in tail if x > pivot]

    return quick_sort_py(arr_left) + [pivot] + quick_sort_py(arr_right)


arr = quick_sort_py(array)
print(arr)
