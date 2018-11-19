n = int(input())
bookStack = list(map(int, input().split()))
vasays = list(map(int, input().split()))
res  = []
b = [False for i in range(0, n + 1)]

for i in range(0, n):
    if b[vasays[i]]:
        res.append("0")
        continue
    for j in range(0, len(bookStack)):
        b[bookStack[j]] = True
        if vasays[i] == bookStack[j]:
           bookStack = bookStack[j + 1 :]
           res.append(str(j + 1))
           break

print(' '.join(res))
