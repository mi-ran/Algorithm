n = int(input())
trees = []
res = 2
for i in range(0, n):
    x, h = list(map(int, input().split()))
    trees.append([x, h])

arr = [0 for i in range(0, trees[-1][0] + 1)]
for a in trees:
    arr[a[0]] = a[1]

for i in range(1, len(arr) - 1):
    if arr[i] is not 0:
        preZero = i - 1
        for j in range(i-1, 0, -1):
            if j is not -1 and arr[j] is not 0:
                break
            preZero = j
        if i - preZero >= arr[i]:
            res = res + 1
        else:
            postZero = i + 1
            for j in range(i+1, len(arr)):
                if j is not len(arr) and arr[j] is not 0:
                    break
                postZero = j
            if postZero - i >= arr[i]:
                res = res + 1
                zero = i + arr[i]
print(res)
    
