import string
line = input()
list_line = [i.lower() for i in line if i not in (string.punctuation+" ")]
print(list_line == list(reversed(list_line)))