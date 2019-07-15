n = int(input())

res = []
for i in range(0, n + 1):
    r = []
    for j in range(0, n-i):
        r.append(" ")
    for k in range(0, i + 1):
        r.append(str(k))
    for l in range(i-1, -1, -1):
        r.append(str(l))
    res.append(r)

for i in range(0, len(res)):
    print(" ".join(res[i]))

for i in range(len(res)-2, -1, -1):
    print(" ".join(res[i]))

