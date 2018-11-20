n = int(input())
bookStack = list(map(int, input().split()))
vasays = list(map(int, input().split()))
res  = []
b = [False for i in range(0, n + 1)]

cur = 0
for i in range(0, n):
    if b[vasays[i]]:
        res.append("0")
        continue
    for j in range(cur, len(bookStack)):
        b[bookStack[j]] = True
        if vasays[i] == bookStack[j]:
           res.append(str(j-cur + 1))
           cur = j + 1
           break

print(' '.join(res))
