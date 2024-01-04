def solution(n):
    matrix = [[0] * n for _ in range(n)]  # n x n 배열 생성
    dx = [0, 1, 0, -1]  # 우, 하, 좌, 상 방향
    dy = [1, 0, -1, 0]
    x, y = 0, 0  # 초기 위치
    direction = 0  # 초기 방향 (우측)

    for i in range(1, n * n + 1):
        matrix[x][y] = i  # 배열에 숫자 채우기
        nx, ny = x + dx[direction], y + dy[direction]  # 다음 위치 계산

        # 다음 위치가 배열을 벗어나거나 이미 값이 채워져 있는 경우 방향 전환
        if nx < 0 or nx >= n or ny < 0 or ny >= n or matrix[nx][ny] != 0:
            direction = (direction + 1) % 4
            nx, ny = x + dx[direction], y + dy[direction]

        x, y = nx, ny  # 다음 위치로 이동

    return matrix

# gpt code
