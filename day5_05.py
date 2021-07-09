# 두개의 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

num_1=int(input())
num_2=input()
num_hund=int(num_2[0])
num_ten=int(num_2[1])
num_one=int(num_2[2])

print(num_1*num_one)
print(num_1*num_ten)
print(num_1*num_hund)
print(num_1*int(num_2))
