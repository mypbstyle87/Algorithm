import math
r = int(input())
h = int(input())

corn_volume = (r ** 2) * math.pi * h / 3

print(round(corn_volume, 3))