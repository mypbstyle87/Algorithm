def solution(s):
    answer = ''
    sentence=s.split()
    for word in sentence:
        count=0
        for letter in word:
            if count%2:
                answer+=letter.lower()
                count+=1
            else:
                answer+=letter.upper()
                count+=1
    return answer


print(solution('pushed        commit    to     originmaster'))
print(solution('        hello world             helalnlv sdnksav sdkfjasdfj asdknasdf         asdkfjasdfn asdkf     '))