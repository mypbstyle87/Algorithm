# 다른 언어에서는..(또는 이 기능을 모르시는 분은)
# 보통 사람들은 for 문을 이용해 숫자를 곱해가며 문제를 풉니다.
#
num = '3212'
base = 5

answer = 0
for idx, number in enumerate(num[::-1]):
    answer += int(number) * (base ** idx)
# 파이썬에서는
# 파이썬의 int(x, base=10) 함수는 진법 변환을 지원합니다.
# 이 기본적인 함수를 잘 쓰면 코드를 짧게 쓸 수 있고, 또 시간을 절약할 수 있습니다.
#
num = '3212'
base = 5
answer = int(num, base)

# 다른 언어에서는..(또는 이 기능을 모르시는 분은)
# 보통 사람들은 나머지와 몫을 따로 구합니다
#
a = 7
b = 5
print(a//b, a%b)
# 파이썬에서는
# 파이썬의 divmod와 unpacking을 이용하면 다음과 같이 코드를 짤 수 있습니다.
#
a = 7
b = 5
print(*divmod(a, b))

# 다른 언어에서는..(또는 이 기능을 모르시는 분은)
# 보통 사람들은 for 문을 이용해 기존 스트링에 공백문자 (' ') 를 여러 번 붙이는 번거로운 일을 하지요. 이렇게요!

### 우측 정렬 예
s = '가나다라'
n = 7

answer = ''
for i in range(n-len(s)): # 문자열의 앞을 빈 문자열로 채우는 for 문
    answer += ' '
answer += s
# 파이썬에서는
# 파이썬에서는 ljust, center, rjust와 같은 string의 메소드를 사용해 코드를 획기적으로 줄일 수 있습니다.
#
s = '가나다라'
n = 7

s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬

print(ord('a'))

# 다른 언어에서는..(또는 이 기능을 모르시는 분은)
# 보통 사람들은 a부터 z까지의 소문자를 가져오려고 할 때, 'abcdefg ....'와 같이 손수 알파벳을 입력하곤 합니다.
#
# answer = 'abcdefghijk (편의상 생략)'
# 파이썬에서는
# 파이썬은 이런 데이터를 상수(constants)로 정의해놓았습니다.
#
import string

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789

# string.ascii_letters
# The concatenation of the ascii_lowercase and ascii_uppercase constants described below. This value is not locale-dependent.
#
# string.ascii_lowercase
# The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not locale-dependent and will not change.
#
# string.ascii_uppercase
# The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not locale-dependent and will not change.
#
# string.digits
# The string '0123456789'.
#
# string.hexdigits
# The string '0123456789abcdefABCDEF'.
#
# string.octdigits
# The string '01234567'.
#
# string.punctuation
# String of ASCII characters which are considered punctuation characters in the C locale.

# 원본을 유지한채, 정렬된 리스트 구하기 - sorted
# 파이썬의 sort() 함수를 사용하면 리스트의 원소를 정렬할 수 있습니다. 이때, sort 함수는 원본의 멤버 순서를 변경하지요.
# 따라서 원본의 순서는 변경하지 않고, 정렬된 값을 구하려면 sort 함수를 사용할 수 없습니다.
#
# 이런 경우는 어떻게 해야 할까요?
#
# 다른 언어에서는..(또는 이 기능을 모르시는 분은)
# 보통 사람들은 deep copy와 sort 함수를 이용합니다.
#
list1 = [3, 2, 1]
list2 = [i for i in list1] # 또는 copy.deepcopy를 사용
list2.sort()
# 파이썬에서는
# 파이썬의 sorted를 사용해보세요. 반복문이나, deepcopy 함수를 사용하지 않아도 새로운 정렬된 리스트를 구할 수 있습니다.
#
list1 = [3, 2, 1]
list2 = sorted(list1)

# 다른 언어에서는..(또는 이 기능을 모르시는 분은)
# 보통은 다음과 같이 2중 for 문을 이용해 리스트의 row와 column을 뒤집습니다.
#
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = [[], [], []]

for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        new_list[i].append(mylist[j][i])
# python에서는
# 파이썬의 zip과 unpacking 을 이용하면 코드 한 줄로 리스트를 뒤집을 수 있습니다.
#
#
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))

# python에서는
# 파이썬의 zip을 이용하면 index를 사용하지 않고 각 원소에 접근할 수 있습니다.

def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer

if __name__ == '__main__':
    mylist = [83, 48, 13, 4, 71, 11]
    print(solution(mylist))
# ※ 주의
#
# zip 함수에 서로 길이가 다른 리스트가 인자로 들어오는 경우에는 길이가 짧은 쪽 까지만 이터레이션이 이루어집니다. 더 자세한 내용은 공식 레퍼런스 - zip의 내용을 참고해주세요.

# 모든 멤버의 type 변환하기 - map
# 이번 강의에서는 Iterable의 모든 멤버의 type을 변환하는 방법을 알아봅시다.
#
# 문자열 배열 ['1', '100', '33']을 정수 배열 [1, 100, 33]로 바꾸기
# 부동소숫점 튜플 (3.14, 3.5, 22.6)을 정수 배열 (3, 3, 22)로 바꾸기
# 다른 언어에서는..(또는 이 기능을 모르시는 분은)
# 보통 사람들은 for 문을 이용해 원소의 타입을 하나씩 바꿉니다.

list1 = ['1', '100', '33']
list2 = []
for value in list1:
    list2.append(int(value))
# 파이썬에서는
# 파이썬의 map을 사용하면 for 문을 사용하지 않고도 멤버의 타입을 일괄 변환할 수 있습니다.

list1 = ['1', '100', '33']
list2 = list(map(int, list1))

# 예시) 두 스트링 'ABCD', 'xy' 의 곱집합은 Ax Ay Bx By Cx Cy Dx Dy 입니다.
#
# 다른 언어에서는..(또는 이 기능을 모르시는 분은)
# 보통 사람들은 for 문을 이용해 두 iterable의 원소를 하나씩 곱해갑니다.

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

for value1 in iterable1:
    for value2 in iterable2:
        for value3 in iterable3:
            print(value1, value2, value3)
# 파이썬에서는
# itertools.product를 이용하면, for 문을 사용하지 않고도 곱집합을 구할 수 있습니다.

import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))

# 가장 많이 등장하는 알파벳 찾기 - Counter
# 알고리즘 문제를 풀다 보면 어떤 원소 x가 주어진 시퀀스타입에 몇 번이나 등장하는지 세야 할 때가 있습니다.
# 이런 경우는 보통 어떻게 하시나요?
#
# 다른 언어에서는..(또는 이 기능을 모르시는 분은)
# 보통 사람들은 반복문을 이용해 수를 셉니다.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = {}
for number in my_list:
    try:
        answer[number] += 1
    except KeyError:
        answer[number] = 1

print(answer[1]) # = 4
print(answer[3])  # = 3
# print(answer[100])  # =  raise KeyError
# 파이썬에서는
# 파이썬의 collections.Counter 클래스를 사용하면 이 코드를 간략하게 만들 수 있습니다.

import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)
print('answer:', answer)
print(type(answer))
print(answer[1]) # = 4
print(answer[3])  # = 3
# print(answer[100]) # = 0