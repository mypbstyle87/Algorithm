burger = [461, 431, 420, 0]
side = [100, 57, 70, 0]
drink = [130, 160, 118, 0]
dessert = [167, 266, 75, 0]

burger_choice = int(input()) - 1
side_choice = int(input()) - 1
drink_choice = int(input()) - 1
dessert_choice = int(input()) -1

total_calories = burger[burger_choice] + side[side_choice] \
                 + drink[drink_choice] + dessert[dessert_choice]
print('Your total Calorie count is '+str(total_calories)+'.')