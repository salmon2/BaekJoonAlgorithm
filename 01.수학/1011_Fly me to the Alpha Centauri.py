num = int(input())

for i in range(num):
    x, y = map(int, input().split())
    lenght = y - x
    k = 1
    count = 0
    move = 0
    while lenght >0:
        count= count +1
        lenght = lenght - k
        if count % 2 == 0:
            k = k +1
    print(count)

