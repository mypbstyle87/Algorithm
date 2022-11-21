monthly_mb = int(input())
n = int(input())
resid = monthly_mb * (n + 1)
for i in range(n):
    spend_mb = int(input())
    resid = resid - spend_mb
print(resid)
