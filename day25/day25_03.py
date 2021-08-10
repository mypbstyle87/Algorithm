
# 정해
def card_conv(x: int, r: int) -> str:
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x % r]
        x //= r

    return d[::-1]

if __name__ == '__main__':
    print('10진수를 n진수로 변환합니다.')

    while True:
        while True:
            no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요.: '))
            if no > 0 and str(no).isdigit():
                break
        while True:
            cd = int(input('어떤 진수로 변환할까요?: '))
            if 2<= cd <= 36:
                break

        print(f'{cd}진수로는 {card_conv(no,cd)}입니다.')

        retry = input("한번 더 변환할까요? (Y/N): ")
        if retry in {'N','n'}:
            break


# 자작ㅋ
# def calc_binary(a: Any):
#     ans_list = []
#     while a // 2 > 0:
#         ans_list.append(a % 2)
#         a = a // 2
#         # print(a)
#     ans_list.append(a % 2)
#     ans_list.reverse()
#     answer = ""
#
#     for i in ans_list:
#         answer += str(i)
#     return int(answer)


# print(calc_binary(59))
#
#
# def calc_octa(a: Any):
