width_unit = int(input())
cheese_contain = int(input())
if width_unit == 3 and cheese_contain >= 95:
    word = 'absolutely'
elif width_unit == 1 and cheese_contain <= 50:
    word = 'fairly'
else:
    word = 'very'

print('C.C. is', word, 'satisfied with her pizza.')
