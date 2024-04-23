from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

distances = [[abs(hx - cx) + abs(hy - cy) for cx, cy in chickens] for hx, hy in houses]

result = float('inf')
for chicken_comb in combinations(range(len(chickens)), m):
    chicken_distance = sum(min(distances[h][c] for c in chicken_comb) for h in range(len(houses)))
    result = min(result, chicken_distance)

print(result)