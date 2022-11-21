first_3point_count = int(input())
first_2point_count = int(input())
first_1point_count = int(input())
second_3point_count = int(input())
second_2point_count = int(input())
second_1point_count = int(input())

first_total_point = first_3point_count *3 + first_2point_count * 2 + first_1point_count
second_total_point = second_3point_count *3 + second_2point_count * 2 + second_1point_count

if first_total_point > second_total_point:
    print("A")
elif first_total_point < second_total_point:
    print("B")
else:
    print("T")
    