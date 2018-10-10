import sys

def func_(arr):
    for i in range(0, len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr) ):
                tmp = arr[i]*100 + arr[j] *10 + arr[k]
                if tmp%8 is 0:
                    print("YES")
                    print(tmp)
                    sys.exit()


def func_2(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            tmp = arr[i]*10 + arr[j]
            if tmp%8 is 0:
                print("YES")
                print(tmp)
                sys.exit()


if __name__ == '__main__':
    arr = list(map(int, input()));
    if 0 in arr:
        print("YES")
        print(0)
        sys.exit()
    elif 8 in arr:
        print("YES")
        print(8)
        sys.exit()

    if len(arr) is 2 or len(arr) is 1:
        tmp = int(''.join([str(i) for i in arr]))
        if tmp%8 is 0:
            print("YES")
            print(tmp)
        else:
            print("NO")
        sys.exit()

    func_(arr)
    func_2(arr)
    print("NO")
