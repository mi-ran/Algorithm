boyN = int(input())
boys = list(map(int, input().split()))
boys.sort()

girlN = int(input())
girls = list(map(int, input().split()))
girls.sort()

res = 0
g = 0
b = 0
while True:
    if g is girlN or b is boyN:
        break
    if boys[b] - girls[g] > 0:
        if boys[b] - girls[g] is 1:
            res = res + 1
            b = b + 1
            g = g + 1
        else:
            g = g + 1
    elif boys[b] - girls[g] < 0:
        if boys[b] - girls[g] is -1:
            res = res + 1
            b = b + 1
            g = g + 1
        else:
            b = b + 1
    else:
        res = res + 1
        b = b + 1
        g = g + 1

print(res)
