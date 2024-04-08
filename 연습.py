def dfs(current_node, graph, visited):
    cnt = 1
    visited[current_node] = True
    for adjacent_node in graph[current_node]:
        if not visited[adjacent_node]:
            cnt += dfs(adjacent_node, graph, visited)
    return cnt
        
def solution(n, wires):
    answer = float('inf')
    graph = [[] for _ in range(n+1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    for i in range(n-1):
        visited = [False] * (n+1)
        v1, v2 = wires[i]
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        cnt1 = dfs(v1, graph, visited)
        cnt2 = n - cnt1
        answer = min(answer, abs(cnt1 - cnt2))
        graph[v1].append(v2)
        graph[v2].append(v1)
    return answer