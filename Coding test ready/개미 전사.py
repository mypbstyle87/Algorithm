n = int(input())
data = list(map(int, input().split()))

food_store = [0] * n

for i in range(n):
    if i <= 1:
        food_store[i] = data[i]
        continue
    elif i == 2:
        food_store[i] = data[0] + data[i]
        continue
    food_store[i] = max(food_store[i - 2], food_store[i - 3]) + data[i]
print(food_store)
print(max(food_store))
