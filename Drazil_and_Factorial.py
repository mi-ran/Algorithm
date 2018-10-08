def addList(a, b):
    return [a[i] + b[i] for i in range(0, len(a))]


def isPrime(n):
    for i in range(2, n):
        if n % i is 0:
            return False
    return True


def Factorial(n):
    arr = [0,0,0,0,0,0,0,0,0,0]
    for i in range(2, n + 1):
        arr[i] = arr[i] + 1
    return arr


def calcArr(arr):
    for i in range(9, 0, -1):
        if isPrime(i):
            for j in range(0, i):
                arr[j] = arr[j] - arr[i]
        else:
            if i % 2 is 0:
                arr[2] = arr[2] + arr[i]
                arr[i//2] = arr[i//2] + arr[i]
                arr[i] = 0
            elif i % 3 is 0:
                arr[3] = arr[3] + arr[i]
                arr[i//3] = arr[i//3] + arr[i]
                arr[i] = 0
    return arr
        

if __name__ == '__main__':
    input()
    str_ = str(input())
    arr = [0,0,0,0,0,0,0,0,0,0]

    for s in str_:
        arr = addList(arr, Factorial(int(s)))
    arr = calcArr(arr)

    res = []
    for i in range(1, 9):
        for j in range(0, arr[i]):
            res.append(str(i))

    res.sort(reverse=True)
    print("".join(res))
            
    
