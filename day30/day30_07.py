num = int(input())
std_list = list(map(int, input().split()))
print(' '.join(map(str,std_list[::-1])))