def dfs(current_node, graph, visited):
    cnt = 1
    visited[current_node] = True
    # 현재노드의 인접노드가 방문되지 않았다면 dfs 재귀 호출 
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
        
        # 간선 제거
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        
        # dfs(현재송전탑, 그래프, 방문여부) 탐색하여 cnt 계산
        cnt1 = dfs(v1, graph, visited)
        cnt2 = n - cnt1
        answer = min(answer, abs(cnt1 - cnt2))  # 최솟값을 구하기 위해 min 함수 사용
        
        # 간선 다시 추가
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    return answer
