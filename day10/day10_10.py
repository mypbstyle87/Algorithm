# 문제1
# 어떤 수(number)의 각 자리 숫자(digit)의 합을 계산하는 sumOfDigits()라는 재귀 함수를 작성하자.
# 입력한 수를 읽어 sumOfDigits() 함수를 호출하며,
# 이 함수는 합산할 숫자가 남지 않을 때까지 자신을 호출해, 최종적인 합을 사용자에게 표시한다.
#
# sumOfDigits()는 다음과 같은 원리로 작동한다.(주의: 실제 코드가 아님)
#
# sumOfDigits(6452) = 2 + sumOfDigits(645)
# sumOfDigits(645) = 5 + sumOfDigits(64)
# ...
# sumOfDigits(6) = 6

# 입력:
# 47253

def sumOfDigits(n):
    if n>=1:
        return n%10 + sumOfDigits(n//10)
    else:
        return 0



print(sumOfDigits(546))

