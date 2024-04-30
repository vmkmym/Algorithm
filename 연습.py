n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

def min_paints(board, n, m):
    result = [] 
    for i in range(n-7): # 8x8 부분 체스판을 선택할 수 있는 모든 경우의 수
        for j in range(m-7):
            count1 = 0 # 첫 번째 칸이 W인 경우
            count2 = 0 # 첫 번째 칸이 B인 경우
            for k in range(i, i+8): # 선택된 8x8 부분 체스판 내의 각 칸을 순회
                for l in range(j, j+8):
                    if (k+l)%2 == 0: # 행과 열의 합이 짝수인 경우
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