num = int(input())

stack = []
res = 0
for i in range(num):
    m = int(input())
    if m != 0:
        stack.append(m)
        res = res + m
    elif m == 0:
        n = stack.pop()
        res = res -n

print(res)