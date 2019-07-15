n = int(input())

nameMap = {}
res = []

for i in range(0, n):
    name = input()
    if name in nameMap:
        nameMap[name] = nameMap[name] + 1
        res.append('%s%d' %(name, nameMap[name]))
    else:
        nameMap[name] = 0
        res.append("OK")

for r in res:
    print(r)
