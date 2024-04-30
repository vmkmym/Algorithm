n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

def min_paints(board, n, m):
    result = [] 
    for i in range(n-7):
        for j in range(m-7):
            count1 = 0
            count2 = 0
            for k in range(i, i+8):
                for l in range(j, j+8):
                    if (k+l)%2 == 0:
                        if board[k][l] != 'W':
                            count1 += 1
                        if board[k][l] != 'B':
                            count2 += 1
                    else:
                        if board[k][l] != 'B':
                            count1 += 1
                        if board[k][l] != 'W':
                            count2 += 1
            result.append(count1)
            result.append(count2)
    return min(result)

print(min_paints(board, n, m))