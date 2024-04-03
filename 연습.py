def find_common_ancestor(tree, node1, node2):
    ancestors = set()
    while node1:
        ancestors.add(node1)
        node1 = tree.get(node1)
    
    while node2:
        if node2 in ancestors:
            return node2
        node2 = tree.get(node2)
    
    return None

# edges 간선을 이용하여 tree 구조를 만든다.
def build_parents(edges):
    tree = {}
    for parent, child in edges:
        tree[child] = parent
    return tree

# 가장 가까운 공통 조상 찾기 
def nearest_common_ancestor(edges, node1, node2):
    tree = build_parents(edges)
    return find_common_ancestor(tree, node1, node2)

# 입력 받기
test_cases = int(input())
for _ in range(test_cases):
    node_count = int(input())
    edges = [list(map(int, input().split())) for _ in range(node_count - 1)]
    node1, node2 = map(int, input().split())
    print(nearest_common_ancestor(edges, node1, node2))