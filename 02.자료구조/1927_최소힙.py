import heapq
import sys

num = int(sys.stdin.readline())

heap = []
for i in range(num):
    q = int(sys.stdin.readline())
    if q == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, q)    