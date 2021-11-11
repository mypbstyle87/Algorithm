import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ['hit']
temp = re.sub(r'[^\w]', ' ', paragraph).lower().split()

words = [word for word in re.sub(r'[\W]', ' ', paragraph).lower().split() if word not in banned]
print(temp)
print(words)