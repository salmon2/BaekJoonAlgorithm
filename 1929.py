import math

m, n = map(int, input().split())

arr = [1 for i in range(n+2)]
arr[0] = 0
arr[1] = 0

for i in range(2, int(math.sqrt(len(arr))+1)):
    if arr[i] == 1:
        for j in range(i+i, len(arr), i):
            arr[j] = 0

for i in range(m, n+1):
    if arr[i] == 1:
        print(i)
