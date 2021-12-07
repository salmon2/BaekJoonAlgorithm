num = int(input())

for i in range(num):
    h, w, n = map(int, input().split())
    y = n % h
    x = n //h +1

    if n % h == 0:
        y = h
        x = n//h

    y = str(y)
    if x < 10:
        x = "0" + str(x)
    else:
        x = str(x)
    print(y+x)