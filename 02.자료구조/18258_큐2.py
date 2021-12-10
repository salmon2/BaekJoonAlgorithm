import sys

num = int(sys.stdin.readline())
q = []
mark = 0

for i in range(num):
    cmd = sys.stdin.readline().strip()
    if cmd.find('push') != -1:
        cmd , n = cmd.split()
        q.append(n)
    elif cmd == "pop":
        if len(q)-mark == 0:
            print(-1)
        else:
            print(q[mark])
            mark = mark + 1 
    elif cmd == "size":
        print(len(q)-mark)
    elif cmd == "empty":
        if len(q)-mark == 0:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if len(q)-mark == 0:
            print(-1)
        else:
            print(q[mark])
    elif cmd == "back":
        if len(q)-mark == 0:
            print(-1)
        else:
            print(q[-1])
