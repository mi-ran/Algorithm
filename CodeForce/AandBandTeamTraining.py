import sys

e, n = list(map(int, input().split()))
res = 0
while True:
    if e + n < 3:
        print(res)
        sys.exit()
    if e is 0 or n is 0:
        print(res)
        sys.exit()
    if e < n:
        n = n - 2
        e = e - 1
        res = res + 1
    else:
        e = e - 2
        n = n - 1
        res = res + 1
print(res)
