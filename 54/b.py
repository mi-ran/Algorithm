import sys
import math
n = int(input())
count = 0
primes = [2]


tmp = True
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        tmp = False
        break
if tmp:
    print(1)
    sys.exit()


while n != 0:
    if n % 2 == 0:
        print(count + n//2)
        sys.exit()

    temp = True
    for p in primes:
        if n % p == 0:
            count = count + 1
            n = n - p
            temp = False
            break
    if not temp:
        continue

    for i in range(primes[-1] + 1, 100000 + 1):
        tt = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                tt = False
                break
        if tt:
            primes.append(i)
            if n % i == 0:
                count = count + 1
                n = n - i
                break
print(count)


