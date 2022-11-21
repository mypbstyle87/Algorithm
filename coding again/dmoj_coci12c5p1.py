line = input()
char_list = []
for i in line:
    char_list.append(i)
main_tone_list = [char_list[0]]
for k, v in enumerate(char_list):
    if v == '|':
        main_tone_list.append(char_list[k + 1])

count_c = main_tone_list.count('C') + main_tone_list.count('F') + main_tone_list.count('G')
count_a = main_tone_list.count('A') + main_tone_list.count('D') + main_tone_list.count('E')
if count_c > count_a:
    print('C-dur')
elif count_a > count_c:
    print('A-mol')
else:
    if char_list[-1] == 'C' or char_list[-1] == 'F' or char_list[-1] == 'G':
        print('C-dur')
    else:
        print('A-mol')
