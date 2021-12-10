import sys

def two(list_):
    list_.append(list_.pop(0))
    return list_
def three(list_):
    list_.insert(0, list_.pop())
    return list_

n, m = map(int, sys.stdin.readline().split())

arr = [i+1 for i in range(n)]

v = list(map(int, sys.stdin.readline().split()))

count = 0
for i in v:
    while True:
        index = arr.index(i)
        lenght = len(arr)
        if arr[0] == i:
            arr.pop(0)
            break
        elif  index - 0 >= lenght - index:
            for h in range(lenght - index):
                arr = three(arr)
                count = count + 1
        elif index - 0 < lenght - index:
            for h in range(index):  
                arr = two(arr)
                count = count +1
print(count)
        