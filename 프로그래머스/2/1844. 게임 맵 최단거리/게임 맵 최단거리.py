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


'''
BFS(Breadth-First Search, 너비 우선 탐색)와 DFS(Depth-First Search, 깊이 우선 탐색)는 그래프 탐색 알고리즘의 두 가지 주요 유형입니다.

BFS는 시작 노드에서 가장 가까운 노드부터 탐색하며, 
모든 인접 노드를 방문한 후에 인접 노드의 인접 노드를 방문하는 방식으로 진행됩니다. 
BFS는 큐를 사용하여 구현할 수 있습니다.

DFS는 시작 노드에서 가장 멀리 있는 노드까지 탐색하며, 더 이상 방문할 노드가 없을 때까지 깊이 우선으로 탐색합니다. 
DFS는 재귀 함수나 스택을 사용하여 구현할 수 있습니다.

BFS가 최단 경로를 찾는 문제에 적합. 
DFS는 모든 경로를 탐색하고자 할 때 적합.
'''