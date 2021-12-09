
a, b, v =  map(int, input().split())

high = v - b
if high%(a-b) == 0:
    day = int(high / (a-b))
else:
    day = int(high/(a-b)) + 1

print(day)

