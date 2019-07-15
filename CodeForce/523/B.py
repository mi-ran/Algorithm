import sys

n,m = list(map(int, input().split()))
a_list = list(map(int, input().split()))
a_list.sort()
right = a_list[-1]

if n == 1:
    print(0)
    sys.exit()

cur = 2
remove = 0
for i in range(0, len(a_list)):
    if a_list[i] == 1:
        continue
    elif a_list[i] < cur:
        remove = remove + 1
        continue
    remove = remove + n - i - 1
    remove = remove + 1
    cur = cur + 1

if n > right:
    remove = remove - (n - right)
print(remove)

