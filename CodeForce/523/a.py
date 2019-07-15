n, S = list(map(int, input().split()))
count = 0
tmp = n
while S > 0:
    value = S//tmp
    if value > 0:
        S = S - tmp*value
        count = count + value
    else:
        tmp = tmp - 1
print(count)
