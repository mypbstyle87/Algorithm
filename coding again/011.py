line = input()
happy_count = line.count(':-)')
sad_count = line.count(':-(')
if happy_count == 0 and sad_count == 0:
    print('none')
elif happy_count > sad_count:
    print('happy')
elif happy_count < sad_count:
    print('sad')
else:
    print('unsure')
