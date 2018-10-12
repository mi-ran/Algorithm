input()
arr = list(map(int, input().split()))

s = sum(arr)
arr.sort(reverse=True)

freq = [0, 0, 0, 0, 0]
for a in arr:
	freq[a] = freq[a] + 1 

res = freq[4]

oneAndThree = min(freq[1], freq[3])
res = res + oneAndThree
freq[1] = freq[1] - oneAndThree
freq[3] = freq[3] - oneAndThree
res = res + freq[3]

if (freq[1] + freq[2]*2) % 4 is not 0:
	res = res + (freq[1] + freq[2]*2)//4 + 1
else:
	res = res + (freq[1] + freq[2]*2)//4


print(res)

