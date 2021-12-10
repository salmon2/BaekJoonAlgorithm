def solution(board, moves):
    answer = 0
    n = len(board)
    x = []
    stack = []
    count = 0
    for i in range(n):
        y = []
        for j in range(n-1,-1,-1):
            if(board[j][i] != 0):
                y.append(board[j][i])
        x.append(y)
    print(x)
    for i in moves:
        if len(stack) != 0 and len(x[i-1]) != 0:
            if stack[-1] == x[i-1][-1]:
                x[i-1].pop()
                stack.pop()
                count = count +1
            else:
                stack.append(x[i-1].pop())
        elif len(x[i-1])!= 0:
            stack.append(x[i-1].pop())
    
    print(count)
    print(stack)

    return answer
solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])