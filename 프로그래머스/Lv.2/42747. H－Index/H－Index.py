def solution(citations):
    citations.sort()
    n = len(citations)
    for h in range(n+1):
        if h <= len([i for i in citations if i >= h]):
            h_index = h
    return h_index


# 다른 사람 풀이
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1))) # enumerate: 인덱스와 값을 동시에 반환
    return answer

# [6, 5, 3, 1, 0] -> [(1, 6), (2, 5), (3, 3), (4, 1), (5, 0)] 
# -> [(1, 6), (2, 5), (3, 3), (4, 1), (5, 0)] -> [1, 2, 3, 1, 0] -> 3
