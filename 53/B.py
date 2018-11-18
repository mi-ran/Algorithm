n = int(input())
bookStack = list(map(int, input().split()))
vasays = list(map(int, input().split()))
res  = []

for i in range(0, n):
    if vasays[i] not in bookStack:
        res.append("0")
        continue
    j = bookStack.index(vasays[i])
    bookStack = bookStack[j + 1 :]
    res.append(str(j+1))

print(' '.join(res))
