# 뮤터블한 리스트의 인덱스 지정 후 값 변경하기

def change(lst,idx,val):
    lst [idx] = val
x = [11, 22, 33, 44, 55]
print('x=', x)

index = int(input(f'업데이트할 인덱스를 선택하세요(0 ~ {len(x)-1}): '))
value = int(input('새로운 값을 입력하세요.: '))

change(x, index, value)
print(f'x= {x}')

