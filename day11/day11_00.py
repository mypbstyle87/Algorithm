# list comprehension

ex_list=[]
for i in range(4):
    ex_list.append(i)
print(ex_list)

ex_list_2=[i for i in range(4)]
print(ex_list_2)

ex_list_3=list(range(4))
print(ex_list_3)

ex_list_4=[]
for i in range(5):
    ex_list_4.append(i*10)
print(ex_list_4)

ex_list_5=[i*10 for i in range(5)]
print(ex_list_5)


def test(x):
    x = str(x) + 'ab'
    return x

ex_list_6=[test(i) for i in range(5)]
print(ex_list_6)

ex_list_7=[i for i in range(5) if i%2==0 if i%4==0] # 조건문을 동시에 쓰면 'and'로 인식된다
print(ex_list_7)

ex_list_8=[i if i%2==0 else 'odd' for i in range(5)] # if else를 쓸때는 for문 왼쪽에 쓴다
print(ex_list_8)

ex_list_9=[i if i%2==0 else 'odd-1' if i==1 else 'odd-3'  for i in range(5)] # if else 가 2번 나오는 경우 가운데 else 조건은 뒤에 있는 if 조건이 만족될때 실행(elif)
print(ex_list_9)

ex_list_10=[(i,j) for i in range(2) for j in range(3)]
print(ex_list_10)

ex_list_11=[i for i in range(10) if i%2==0]
print(ex_list_11)

# zip 함수
l = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9]
l3 = [10, 11, 12]

ex_list_12=[(v, v2, v3) for v, v2, v3 in zip(l, l2, l3)]
print(ex_list_12)