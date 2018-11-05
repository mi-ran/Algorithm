riders, taxi_drivers = list(map(int, input().split()))
points = list(map(int, input().split()))
who = list(map(int, input().split()))

taxi_driver_points = []
res = []
for i in range(0, len(who)):
    if who[i] is 1:
        taxi_driver_points.append(points[i])
        res.append(0)

cur = 0
for i in range(0, len(who)):
    if who[i] is 0:
        if cur is len(res) - 1:
            res[cur] = res[cur] + 1
        else:
            diff1 = taxi_driver_points[cur] - points[i]
            diff2 = taxi_driver_points[cur + 1] - points[i]

            if diff1 < 0:
                diff1 = diff1 * -1
            if diff2 < 0:
                diff2 = diff2 * -1

            if diff1 > diff2:
                cur = cur + 1
            res[cur] = res[cur] + 1
    else:
        if i is not len(who) - 1 and who[i + 1] is 1:
            cur = cur + 1

res_ = [str(r) for r in res]
res_str = " ".join(res_)
print(res_str)
            
