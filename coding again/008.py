first_number = int(input())
second_number = int(input())
third_number = int(input())
fourth_number = int(input())

if first_number == 8 or first_number == 9:
    if fourth_number == 8 or fourth_number == 9:
        if second_number == third_number:
            print('ignore')
        else:
            print('answer')
    else:
        print('answer')

else:
    print("answer")
