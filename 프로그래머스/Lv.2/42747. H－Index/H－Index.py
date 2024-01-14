def solution(citations):
    citations.sort()
    n = len(citations)
    for h in range(n+1):
        if h <= len([i for i in citations if i >= h]):
            h_index = h
    return h_index