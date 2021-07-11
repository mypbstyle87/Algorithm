# 문자열의 숫자 판별법 isdecimal() isnumeric()
a="123456"
print(a.isdecimal())
b="123b456"
print(b.isdecimal())

# 아스키 변환 내장함수
print(ord("a"))

# enumerate
# 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 수 있습니다. 이때 사용합니다.
# 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환합니다.

t = [1, 5, 7, 33, 39, 52]
for p in enumerate(t):
    print(p)

# tuple형태 반환을 이용하여 아래처럼 활용할 수 있습니다.
# >>> for i, v in enumerate(t):
# ...     print("index : {}, value: {}".format(i,v))