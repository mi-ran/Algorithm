def search(arr, target, start, end):
    idx = (start + end)//2
    while True:
        if arr[idx] is target:
            print(idx + 1)
            return
        elif arr[idx] > target:
            if idx is 0 or arr[idx - 1] < target:
                print(idx + 1)
                return
            return search(arr, target, start, (start + end)//2)
        elif arr[idx] < target:
            return search(arr, target, (start + end)//2, end)
        

if __name__ == "__main__":
    a = int(input())
    aList = list(map(int, input().split()))

    arr = [aList[0]]
    for i in range(1, len(aList)):
        arr.append(arr[i-1] + aList[i])

    b = int(input())
    bList = list(map(int, input().split()))

    for i in bList:
        search(arr, i, 0, len(aList))

