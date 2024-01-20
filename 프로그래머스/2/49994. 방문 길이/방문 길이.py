def solution(dirs):
    moves = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    visited = set()
    x, y = (0, 0)

    for move in dirs:
        dx, dy = moves[move] # 이동 방향
        nx, ny = x + dx, y + dy # 이동 후 좌표
        if -5 <= nx <= 5 and -5 <= ny <= 5: # 좌표가 범위 내에 있으면
            if (x, y, nx, ny) not in visited: # 방문하지 않았으면
                visited.add((x, y, nx, ny)) # 갔던 길과
                visited.add((nx, ny, x, y)) # 되돌아가는 길 모두 방문처리
            x, y = nx, ny

    return len(visited) // 2