swaps = input()
p = 1

for swap_type in swaps:
    if swap_type == 'A' and p == 1:
        p = 2
    elif swap_type == 'A' and p == 2:
        p = 1
    elif swap_type == 'B' and p == 2:
        p = 3
    elif swap_type == 'B' and p == 3:
        p = 2
    elif swap_type == 'C' and p == 1:
        p = 3
    elif swap_type == 'C' and p == 3:
        p = 1

print(p)
