import array as arr

int_arr = arr.array('i', [2, 3, 6, 10])
input_num = int(input())

for i in range(len(int_arr)):
    for j in range(i + 1, len(int_arr)):
        if int_arr[i] + int_arr[j] == input_num:
            print(i, j)


