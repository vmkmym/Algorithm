def solution(m, n, board):
    board = [list(x) for x in board]
    matched = True
    while matched:
        # 1) Find 2x2 blocks
        matched = []
        for i in range(m-1): 
            for j in range(n-1):
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != '#': # 2x2 블록이 같은 경우
                    matched.append([i, j]) # 2x2 블록의 좌상단 좌표를 matched에 추가
        # 2) Mark 2x2 blocks
        for i, j in matched: # 2x2 블록의 좌상단 좌표를 가져온다.
            board[i][j] = board[i][j+1] = board[i+1][j] = board[i+1][j+1] = '#' # 2x2 블록을 #으로 표시
        # 3) Gravity
        for _ in range(m): # 행의 개수만큼 반복
            for i in range(m-1): # 행의 개수만큼 반복
                for j in range(n): # 열의 개수만큼 반복
                    if board[i+1][j] == '#': # 아래가 #이면
                        board[i+1][j], board[i][j] = board[i][j], '#' # 아래와 자리를 바꾼다.
    return sum(x.count('#') for x in board) # #의 개수를 센다.