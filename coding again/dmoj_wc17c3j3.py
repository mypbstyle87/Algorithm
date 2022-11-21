password = input()
word_length = len(password)
lower_count = 0
upper_count = 0
digit_count = 0
if 8 <= word_length <= 12:
    for char in password:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
        else:
            digit_count += 1
    if lower_count >= 3 and upper_count >= 2 and digit_count >= 1:
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")
