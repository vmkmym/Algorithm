def solution(board):
    rows = len(board)
    cols = len(board[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    safe_count = sum(
        all(board[i + dx][j + dy] == 0 for dx, dy in directions if is_valid(i + dx, j + dy))
        for i in range(rows)
        for j in range(cols)
        if board[i][j] == 0
    )
    
    return safe_count