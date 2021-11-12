array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:  # array[j]가 전항보다 작은 한, 앞으로 한칸씩 계속 이동
            array[j], array[j - 1] = array[j - 1], array[j] # 스와프
        else:
            break  # array[j]가 전항보다 크면 멈춤

print(array)
