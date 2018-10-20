def search(arr, target, start, end):
    idx = (start + end)//2
    while True:
        if arr[idx] is target:
            print(arr[idx], end=' ')
            return
        elif arr[idx] > target:
            if arr[idx - 1] < target:
                print(arr[idx], end=' ')
                return
            search(arr, target, start, (start + end)//2)
        elif arr[idx] > target:
            search(arr, target, (start + end)//2, end)
        

if __name__ == "__main__":
    a = int(input())
    aList = list(map(int, input().split()))

    arr = [aList[0]]
    for i in range(1, len(aList)):
        arr.append(arr[i-1] + aList[i])

    b = int(input())
    bList = list(map(int, input().split()))

    idx = len(aList)//2
    for i in bList:
        search(aList, i, 0, len(aList)//2)


