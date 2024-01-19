def solution(n, computers):
    parent = list(range(n)) # 각 노드의 부모 노드를 저장하는 리스트(초기에는 자기 자신이 부모 노드)

    # 주어진 노드의 부모 노드를 찾는 함수
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    # 두 노드의 루트 노드가 다르면 두 노드를 연결하는 함수
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x

    # 모든 노드를 순회하며 두 노드를 연결하는 함수를 호출
    for i in range(n):
        for j in range(n): 
            # i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현
            if computers[i][j] == 1:
                union(i, j)

    for i in range(n):
        find(i)
    
    return len(set(parent))