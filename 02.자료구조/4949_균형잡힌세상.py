def solution():
    while True:
        p = input()
        if p == '.':
            return 0
        stack = []
        for i in p:
            if p == '.':
                break
            if i == '(' or i == '[':
                stack.append(i)
            elif i == ')':
                if len(stack) == 0:
                    stack.append(i)
                else:
                    res = stack[-1]
                    if res != '(':
                        stack.append(i)
                    elif res == '(':
                        stack.pop()
            elif i == ']':
                if len(stack) == 0:
                    stack.append(i)
                else:
                    res = stack[-1]
                    if res != '[':
                        stack.append(i)
                    elif res == '[':
                        stack.pop()

        if len(stack) == 0:
            print('yes') 
        else:
            print('no')

solution()

