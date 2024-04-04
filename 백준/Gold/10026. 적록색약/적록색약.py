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
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and array[nx][ny] == color:
                stack.append((nx, ny))

def count_regions(color):
    count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and array[i][j] == color:
                dfs(i, j, color)
                count += 1
    return count

sum1 = count_regions('R') + count_regions('G') + count_regions('B')

for i in range(n):
    for j in range(n):
        if array[i][j] == 'G':
            array[i][j] = 'R'

visited = [[0] * n for _ in range(n)]
sum2 = count_regions('R') + count_regions('B')

print(sum1, sum2)