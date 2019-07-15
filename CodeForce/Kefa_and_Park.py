def visite(dic, vs, current, cnt, con):
    if vs[current] is 1:
        cnt = cnt - 1
    else:
        cnt = con

    res = 0
    if current in arr:
        for p in arr[current]:
            res =  res + visite(dic, vs, p, cnt, con)
    else:
        if cnt >= 0:
            return res + 1
    return res
        



if __name__ == '__main__':
    number_of_v, con = list(map(int, input().split()))
    vs = list(map(int, input().split()))

    arr = {}
    leaf = [True for i in range(0, number_of_v)]

    for i in range(0, number_of_v - 1):
        f, t = list(map(int, input().split()))
        if t - 1 in arr:
            arr[t-1].append(f-1)
        else:
            arr[t-1] = [f -1]
        leaf[f-1] = False

    res = 0
    for i in range(0, number_of_v):
        if leaf[i] == True:
            res = res + visite(arr, vs, i, con, con)
    print(res)

