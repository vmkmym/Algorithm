from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우, 하, 좌, 상
    queue = deque([(0, 0, 1)])  # (x, y, 이동 횟수)

    while queue:
        x, y, count = queue.popleft() # 큐의 가장 앞에 요소 반환 후 제거
        
        if x == n - 1 and y == m - 1:  # 도착지에 도달하면 이동 횟수 반환
            return count
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy # 4가지 방향을 현재 좌표에 넣어서 이동가능하면 방문 표시 후 큐에 현재 좌표와 이동 횟수 저장
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:  # 이동 가능하면
                maps[nx][ny] = 0  # 방문 표시
                queue.append((nx, ny, count + 1))  # 큐에 추가

    return -1