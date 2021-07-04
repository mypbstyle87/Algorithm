# 세 정수를 입력받아 중앙값 구하기1

def med3(a,b,c):
    """a,b,c 의 중앙값을 구하여 반환"""
    temp_list=[]
    temp_list.append(a)
    temp_list.append(b)
    temp_list.append(c)
    temp_list.sort()
    return temp_list[1]

print('세 정수의 중앙값을 구합니다.')
a=int(input('정수 a의 값을 입력하세요: '))
b=int(input('정수 b의 값을 입력하세요: '))
c=int(input('정수 c의 값을 입력하세요: '))

print(f'세 정수의 중앙값은 {med3(a,b,c)}입니다.')