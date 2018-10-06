from operator import itemgetter

n = int(input())
tests = []
for i in range(0, n):
	a, b = list(map(int, input().split()))
	tests.append([a, b])

tests.sort(key=itemgetter(0, 1))

cur_date = min(tests[0])
for test in tests:
	if test[1] >= cur_date:
		cur_date = test[1]
	else:
		cur_date = test[0]

print(cur_date)

