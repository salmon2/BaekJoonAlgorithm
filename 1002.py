import math

num = int(input())

for i in range(num):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    xd = abs(x1 - x2)
    yd = abs(y1 - y2)
    d = math.sqrt(xd**2 + yd**2)
    
    if d == 0 and r1 == r2:
        result = -1
    elif (d > r1 + r2 or d < abs(r1 - r2)):
        result = 0
    elif (d == r1 + r2 or d == abs(r1 - r2)):
        result = 1
    elif (d < r1 + r2):
        result = 2


    print(result)