# 이상한 문자 만들기
# 문제 설명
# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
# 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
#
# 제한 사항
# 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
# 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
# 입출력 예
# s	return
# "try hello world"	"TrY HeLlO WoRlD"

def solution(s):
    answer = []
    temp_word = ''
    sentence = s.split(" ")
    for word in sentence:
        count = 0
        for letter in word:
            if count % 2:
                temp_word += letter.lower()
                count += 1
            else:
                temp_word += letter.upper()
                count += 1
        answer.append(temp_word)
        temp_word = ''
    return " ".join(answer)

# 타인의 풀이
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

print(solution("try hello world"))
