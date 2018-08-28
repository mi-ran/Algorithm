#!/usr/bin/python

if __name__ == '__main__':
    data = int(input())
    inputs = list(map(int, input().split())) 

    s = 1
    nums = [1]
    for i in range(0, data - 1):
        if inputs[i]*2 >= inputs[i+1]:
            s = s + 1  
        else:
            nums.append(s)
            s = 1
    nums.append(s) 
    print(max(nums))
