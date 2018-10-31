n = int(input())
l = list(map(int, input().split()))

k = max(l)
e_votes = sum(l)
a_votes = k*n - e_votes

diff = e_votes - a_votes

if diff < 0:
    print(k)
else:
    tmp = diff//n
    print(tmp + k + 1)
