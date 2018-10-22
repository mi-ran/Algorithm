n = input()
arr = list(map(int, input().split()))

for i in arr:
	prime = 2
	for j in range(2 , i):
		if i % j is 0:
			prime = prime + 1
		if prime > 3:
			print("NO")
			break;
	if prime is 2:
		print("NO")
	elif prime is 3:
		print("YES")

