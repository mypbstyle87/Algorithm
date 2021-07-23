# 1~12까지 8을 건너뛰고 출력하기 1

# 비효율
for i in range(1,13):
    if i!=8:
        print(i, end=" ")
print()
# 효율
for i in list(range(1,8))+list(range(9,13)):
    print(i, end=" ")
print()