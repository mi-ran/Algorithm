import sys

m, s = list(map(int, input().split()))
if m is 1 and s is 0:
	print("0 0")
	sys.exit()

if m*9 < s or s is 0:
	print("-1 -1")
	sys.exit()

max_val = []
max_n = 9
temp_s = s
temp_m = m
sum_ = 0
while temp_m is not 0:
	if temp_s >= max_n:
		temp_s = temp_s - max_n
		max_val.append(str(max_n))
		temp_m = temp_m - 1
		sum_ = sum_ + max_n
	elif temp_s is 0:
		max_val.append(str(0))
		temp_m = temp_m - 1
	else:
		max_n = max_n - 1


min_val = [0 for i in range(0, m)]
last = m - 1
for i in range(0, s):
	if i is 0:
		min_val[i] = 1
	elif min_val[last] < 9:
		min_val[last] = min_val[last] + 1
	else:
		last = last - 1
		if last < 0:
			print("-1 -1")
			sys.exit()
		min_val[last] = min_val[last] + 1

min_val.sort()
if min_val[0] is 0:
	for i in range(1, len(min_val)):
		if min_val[i] is not 0:
			tmp = min_val[i]
			min_val[i] = 0
			min_val[0] = tmp
			break

print('%s %s' %("".join(str(x) for x in min_val), "".join(max_val)))



