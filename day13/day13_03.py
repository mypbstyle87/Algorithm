# 자료구조와 함꼐 배우는 알고리즘 입문 p42

print("*를 출력합니다.")
num = int(input("몇개 출력할까요?"))
width = int(input("한줄에 몇개씩 출력할까요?"))

for _ in range(num // width):
    print("*" * width)
if num%width:
    print("*" * (num % width))

