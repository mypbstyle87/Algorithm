list_input = ['h', 'e', 'l', 'l', 'o']
for i in range(len(list_input)//2):
    temp = list_input[i]
    list_input[i] = list_input[-i -1]
    list_input[-i -1] = temp

print(list_input)