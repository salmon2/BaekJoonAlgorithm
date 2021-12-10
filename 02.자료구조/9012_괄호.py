num = int(input())

for i in range(num):
    stack = []
    p = input()
    for i in p:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                stack.append(i)
            else:
                res = stack[-1]
                if res != '(':
                    stack.append(i)
                else:
                    stack.pop()
    if len(stack) == 0:
        print('YES') 
    else:
        print('NO')

