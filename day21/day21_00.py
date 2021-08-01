# 파이썬 람다(lambda) 함수
a = lambda x , y : x * y
print(a(3,4))


# 제곱수가 가장 작은 순서대로 소팅을 하고 싶다.
b = [ -1, -8, 3, -4, 2, 5, -7]
b.sort(key=lambda x : x*x,reverse=True)
print(b)

