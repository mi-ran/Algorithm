n = int(input())

res = n
for i in range(0, n):
    res = res + (n - i) * i

print(res)
