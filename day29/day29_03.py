# 1. for 사용

# temp_list = [1, 2, 3, 4, 5]
# result = []

# def plus_two(x):
#     return x + 2

# for i in temp_list:
#     result.append(plus_two(i))

# result = list(map(plus_two, temp_list))
# print(result)

# 2. for -> map 사용

# result = list(map(plus_two, temp_list))
# print(result)

# 3. map, lambda 함수 사용

# result = list(map(lambda x: x + 2, temp_list))
# print(result)

# 4. map, lambda, range 사용

result = list(map(lambda x: x + 2, range(1, 6)))
print(result)
