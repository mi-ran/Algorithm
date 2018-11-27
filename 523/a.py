n, S = list(map(int, input().split()))
count = 0
tmp = n
while S > 0:
    if S >= tmp:
        S = S - tmp
        count = count + 1
    else:
        tmp = tmp - 1
print(count)
