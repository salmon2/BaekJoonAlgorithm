n, m = map(int, input().split())

arr = [i for i in range(1,n+1)]

i = 0
res = []
while len(arr) != 0:
    lenght = len(arr)
    i = (i + m - 1) % lenght
    res.append(arr.pop(i))

print('<'+', '.join(map(str, res))+'>')
    