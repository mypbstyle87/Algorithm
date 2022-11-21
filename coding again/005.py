paint_left = int(input())
each_paint_spent = int(input())
each_badge_pokedollar = int(input())

num_badge = paint_left // each_paint_spent
left_paint = paint_left % each_paint_spent
total_pokedollar = num_badge * each_badge_pokedollar + left_paint

print(total_pokedollar)
