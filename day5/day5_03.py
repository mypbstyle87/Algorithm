# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B(몫), 다섯째 줄에 A%B를 출력한다.
# split 뒤에 () 주의
c=input().split()

a=int(c[0])
b=int(c[1])

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)

