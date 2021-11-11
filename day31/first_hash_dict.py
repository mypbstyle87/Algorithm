import array as arr
hashdict = {}

int_arr = arr.array('i', [2, 3, 6, 10])
input_num = int(input())

for i in range(0,len(int_arr)):
    if input_num - int_arr[i] in hashdict:
        ans_list = sorted([i, hashdict[input_num - int_arr[i]]])
        print(ans_list)
        quit()
    else:
        hashdict[int_arr[i]] = i
