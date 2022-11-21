# 정수
output_a = "{:d}".format(52)

# 특정 칸에 출력하기
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)

# 빈칸을 0으로 채우기
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

# 기호와 함께 출력하기
output_f = "{:+d}".format(52)  # 양수
output_g = "{:+d}".format(-52) # 음수
output_h = "{: d}".format(52)  # 양수
output_i = "{: d}".format(-52) # 음수

# 조합하기
output_j = "{:+5d}".format(52)    # 기호를 뒤로 밀기: 양수
output_k = "{:+5d}".format(-52)   # 기호를 뒤로 밀기: 음수
output_l = "{:=+5d}".format(52)   # 기호를 앞으로 밀기: 양수
output_m = "{:=+5d}".format(-52)  # 기호를 앞으로 밀기: 음수
output_n = "{:+05d}".format(52)   # 0으로 채우기: 양수
output_o = "{:+05d}".format(-52)  # 0으로 채우기: 음수

# 소숫점 아래 자릿수 지정하기
output_p = "{:15.3f}".format(52.273)
output_q = "{:15.2f}".format(52.273)
output_r = "{:15.1f}".format(52.273)
output_s = "{:15g}".format(52.273000000)

print("# 기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)
print('# 기호와 함께 출력하기')
print(output_f)
print(output_g)
print(output_h)
print(output_i)
print('# 조합하기')
print(output_j)
print(output_k)
print(output_l)
print(output_m)
print(output_n)
print(output_o)
print('# 소숫점 아래 자릿수 지정하기')
print(output_p)
print(output_q)
print(output_r)
print(output_s)