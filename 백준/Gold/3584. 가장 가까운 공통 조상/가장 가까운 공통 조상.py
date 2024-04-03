def find_common_ancestor(parents, node1, node2):
    ancestors = set()
    while node1:
        ancestors.add(node1)
        node1 = parents.get(node1)
    
    while node2:
        if node2 in ancestors:
            return node2
        node2 = parents.get(node2)
    
    return None

def build_parents(edges):
    parents = {}
    for parent, child in edges:
        parents[child] = parent
    return parents

def nearest_common_ancestor(edges, node1, node2):
    parents = build_parents(edges)
    return find_common_ancestor(parents, node1, node2)

# 입력 받기
test_cases = int(input())
for _ in range(test_cases):
    node_count = int(input())
    edges = [list(map(int, input().split())) for _ in range(node_count - 1)]
    node1, node2 = map(int, input().split())
    print(nearest_common_ancestor(edges, node1, node2))
