def solution(citations):
    citations.sort()
    n = len(citations)
    for h in range(n+1):
        if h <= len([i for i in citations if i >= h]):
            h_index = h
    return h_index

# 정렬 문제인데 정렬 안해도 풀리지만,, 통과는 못함
# 정렬을 왜 해야하지? -> h번 이상 인용된 논문이 h편 이상이어야 하기 때문에?


# 다른 사람 풀이
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1))) # enumerate: 인덱스와 값을 동시에 반환
    return answer

# [6, 5, 3, 1, 0] -> [(1, 6), (2, 5), (3, 3), (4, 1), (5, 0)] 
# -> [(1, 6), (2, 5), (3, 3), (4, 1), (5, 0)] -> [1, 2, 3, 1, 0] -> 3
