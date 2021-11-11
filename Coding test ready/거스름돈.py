price = int(input())
coin_count = 0
currency = [500, 100, 50, 10]
for i in currency:
    if price >= i:
        coin_count += price // i
        price %= i
print(coin_count)
