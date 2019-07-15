n, t = list(map(int, input().split()))
s = input()
arr = [i for i in s]

for i in range(0, t):
    j = 0
    while j < n - 1:
        if arr[j] == "B" and arr[j + 1] == "G":
            arr[j] = "G"
            arr[j + 1] = "B"
            j = j + 2
        else:
            j = j + 1

print("".join(arr))
