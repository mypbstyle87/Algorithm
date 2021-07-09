# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.


c = input().split()
num_1=int(c[0])
num_2=int(c[1])
num_3=int(c[2])
print((num_1 + num_2) % num_3)
print((num_1 % num_3 + num_2 % num_3) % num_3)
print((num_1 * num_2) % num_3)
print(((num_1 % num_3) * (num_2 % num_3)) % num_3)

# 결론 : 합의 나머지는 각각의 나머지의 합의 나머지와 같다.
# 결론 : 곱의 나머지는 각각의 나머지의 곱의 나머지와 같다.