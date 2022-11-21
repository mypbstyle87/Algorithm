x = int(input())
d = [0] * 30001  # 연산된 값이 아니라, 연산된 횟수를 저장하는 테이블

for i in range(2, x + 1):
    # 일단 빼는 연산 실행
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
 