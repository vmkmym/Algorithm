import sys

input = sys.stdin.readline
n = int(input())
array = [list(input().strip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
sum1 = 0
sum2 = 0

def dfs(x, y, color):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        visited[x][y] = 1 # 방문 처리
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # nx, ny가 범위 내에 있고, 방문하지 않았으며, 색깔이 같다면
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and array[nx][ny] == color:
                stack.append((nx, ny))

def count_regions(color):
    count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and array[i][j] == color: # 방문하지 않았고, 색깔이 같다면
                dfs(i, j, color) # dfs 탐색으로 방문 처리
                count += 1
    return count

sum1 = count_regions('R') + count_regions('G') + count_regions('B')

for i in range(n): # 초록색을 빨간색으로 변경
    for j in range(n):
        if array[i][j] == 'G':
            array[i][j] = 'R'

visited = [[0] * n for _ in range(n)] # 방문 초기화
sum2 = count_regions('R') + count_regions('B')

print(sum1, sum2)