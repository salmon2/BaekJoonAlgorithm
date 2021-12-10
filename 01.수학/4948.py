import math
n = 123456
arr = [1 for i in range(2*n+1)]
arr[0] = 0
arr[1] = 0

for i in range(2, int(math.sqrt(len(arr)))):
    if arr[i] == 1:
        for j in range(i+i, len(arr), i):
            arr[j] = 0

while True:
    n = int(input())

    if n == 0:
        break
    else:
        print(sum(arr[n+1:(2*n)+1]))

