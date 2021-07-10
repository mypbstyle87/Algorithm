# 입력받은 정수의 부호 출력하기
try:
    num = int(input("정수를 입력하세요: "))
    if num > 0:
        print("양수입니다.")

    elif num == 0:
        print("0입니다.")

    else:
        print("음수입니다.")

except:
    print("정수를 입력하세요.")


