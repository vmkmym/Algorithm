import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
gender = input().split()
edges = []

for _ in range(m):
    u, v, d = map(int, input().split())
    edges.append((d, u, v))

edges.sort()
parent = [i for i in range(n + 1)]
result = 0

for edge in edges:
    cost, a, b = edge
    if gender[a - 1] != gender[b - 1] and find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

for i in range(2, n + 1):
    if find(parent, i) != find(parent, 1):
        print(-1)
        sys.exit()

print(result)