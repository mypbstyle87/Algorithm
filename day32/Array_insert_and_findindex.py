nums_array = [1,2,3,4,5]
nums_dict = {v:k for k, v in enumerate(nums_array)}
# nums_dict.update(zip(range(len(nums_array)), nums_array))

target = int(input())
for i in nums_dict:
    if i >= target:
        print(nums_dict[i])
        break
else:
    print(len(nums_dict))